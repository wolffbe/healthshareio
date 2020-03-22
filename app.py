from flask import Flask, render_template, json, request, url_for, redirect, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import requests
from flask_cors import CORS, cross_origin

app = Flask(__name__)
mydb = mysql.connector.connect(
        host=,
        user=,
        passwd=, 
        database =
    )       

print(mydb)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

print(mydb)
app.config['JSON_SORT_KEYS']=False
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def showSignUp():
     
    if request.method=='POST': 
         #setzen der variablen
        details = request.form
        inputName = details['inputName']
        inputAddress = details['inputAdress']
        inputContact = details['inputAnsprechpartner']
        inputTelephone = details['inputTelephone']
        inputGive= details['inputGive']
        inputAnzahlGive = details['inputAnzahlGive']


        #set institution type
        if details['inputInstitution'] == "Medizinische Einrichtung": 
            institutionType = "medical"
        elif details['inputInstitution'] == "Unternehmen": 
            institutionType =  "company"
        else: 
            institutionType="undefined"
        

        #sql statement preparation
        sql_institution = "INSERT INTO tbl_institutions (name, type, address, contact, telephone, lat, lng) VALUES(%s,%s,%s,%s,%s,%s,%s)"

        values_institution = (inputName, institutionType,inputAddress, inputContact, inputTelephone, 0.0, 0.0)

        print(sql_institution)
        print(values_institution)
        
        cur = mydb.cursor()
        
        try: 
            #execution of insert statement
            cur.execute(sql_institution, values_institution)
            mydb.commit()
            inst_id = cur.lastrowid
            #print("bis hier ok")

        except Exception as e: 
            error = "Something went wrong while inserting the data into tbl_institution"
            print(error)
            print(e)
            return render_template('signup.html', error=error)
        
        
        #set object type 
        objecttypes = [{"Desinfektionsmittel":"disinfectants"}, {"Masken" : "masks"}, {"Handschuhe": "gloves"}]
        
        # if the user wants to add a need
        # if inputNeed and inputAnzahlNeed: 
        #     for object in objecttypes: 
        #         for key in object: 
        #             if inputNeed == key:
        #                 objecttypeDB = object[key]
        
        # #print(objecttypeDB)  
        #     #insert into demand table - statement preparation
        #     sql_demand= "INSERT INTO tbl_demand(fk_institutionid, objecttype, amount) VALUES (%s, %s,%s)"

        #     values_demand=(inst_id, objecttypeDB, inputAnzahlNeed )
        #     print(sql_demand)
        #     print(values_demand)
        #     print(inst_id)
        #     try: 
        #         #insert into demand table - statement execution
        #         cur.execute(sql_demand, values_demand)
        #         mydb.commit()
        #         print("bis hier ist ok")
        #     except Exception as e: 
        #         error = "Something went wrong while inserting the data into tbl_demand"
        #         print(error)
        #         print(e)
        #         return render_template('signup.html', error=error)
        #if the user wants to add a supply 
        if inputGive and inputAnzahlGive:
            for object in objecttypes: 
                for key in object: 
                    if inputGive == key:
                        objecttypeDB = object[key]

            sql_supply= "INSERT INTO tbl_supply(fk_institutionid, objecttype, amount) VALUES (%s, %s,%s)"

            values_supply=(inst_id, objecttypeDB, inputAnzahlGive )
            print(sql_supply)
            print(values_supply)
            print(inst_id)
            try: 
                #insert into demand table - statement execution
                cur.execute(sql_supply, values_supply)
                mydb.commit()
                print("bis hier ist ok")
            except Exception as e: 
                error = "Something went wrong while inserting the data into tbl_demand"
                print(error)
                print(e)
                return render_template('signup.html', error=error)

        return redirect("/map")    


    elif request.method=='GET':
        return render_template('signup.html')

@app.route('/login',methods=['GET','POST'])
def showLogin():    
    return render_template('login.html') 

@app.route('/map')
def showMap():
    return render_template('map.html')
  
@app.route('/profile')
def showProfile():
    return render_template('profile.html')

@app.route('/delivery', methods=['GET','POST'])
def showDelivery():
    #changing of the colours in the traffic lights
    if request.method == 'POST': 
        beitrag="/static/img/green.png"
        versand="/static/img/yellow.png"
        welcometext="Vielen Dank für Ihre Spende!"
        return render_template('delivery.html', beitrag=beitrag, versand=versand, welcometext=welcometext)

    elif request.method=="GET":
        versand="/static/img/red.png"
        beitrag="/static/img/yellow.png"
        welcometext="Jetzt Beitrag konfigurieren!"
        return render_template('delivery.html', beitrag=beitrag, versand=versand, welcometext=welcometext)

@app.route('/deliveries')
def showDeliveries():    
    return render_template('deliveries.html')

@app.route('/mapPoints') #retrieve map points in the database
def getMapPoints():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM tbl_institutions") #Mquery MySQLDB

    myresult = mycursor.fetchall() 
    payload = []
    
    content = {}

    for result in myresult: #create content for JSON
        content = {'id': result[0], 'name': result[1], 'address': result[3], 'lat': result[6], 'lng': result[7], 'type': result[2], 'market' : 'demand', 'disinfectant' : str(0) , 'gloves' : str(0), 'masks': str(0)}
        sql=f'SELECT objecttype, SUM(amount) FROM tbl_demand WHERE fk_institutionid = {result[0]} GROUP BY objecttype;'
        mycursor.execute(sql)
        result_demand = mycursor.fetchall()
        for demandtype in result_demand:
            content[demandtype[0]]= str(demandtype[1])
        payload.append(content)
        content = {}

    print(payload)
    return jsonify(payload)
#start app
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)
from flask import Flask, render_template, json, request, url_for, redirect, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import requests
import mysql.connector
from flask_cors import CORS, cross_origin

app = Flask(__name__)
mydb = mysql.connector.connect(
        host="52.166.36.96",
        user="app",
        passwd="covid789", 
        database ="hackathon"
    )       

print(mydb)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mydb = mysql.connector.connect(
        host="52.166.36.96",
        user="app",
        passwd="covid789", 
        database ="hackathon"
    )

print(mydb)
app.config['JSON_SORT_KEYS']=False
app.config['JSON_AS_ASCII'] = False


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def showSignUp():
    #bei Get soll er das nur rendern .. 
    if request.method=='POST': 
         #setzen der variablen

        details = request.form
        inputName = details['inputName']
        inputAddress = details['inputAdress']
        inputContact = details['inputAnsprechpartner']
        inputTelephone = details['inputTelephone']
        inputNeed = details['inputNeed']
        inputAnzahlNeed = details['inputAnzahlNeed']
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
        
        if inputNeed and inputAnzahlNeed: 
            for object in objecttypes: 
                for key in object: 
                    if inputNeed == key:
                        objecttypeDB = object[key]
        
        #print(objecttypeDB)  
            #insert into demand table - statement preparation
            sql_demand= "INSERT INTO tbl_demand(fk_institutionid, objecttype, amount) VALUES (%s, %s,%s)"

            values_demand=(inst_id, objecttypeDB, inputAnzahlNeed )
            print(sql_demand)
            print(values_demand)
            print(inst_id)
            try: 
                #insert into demand table - statement execution
                cur.execute(sql_demand, values_demand)
                mydb.commit()
                print("bis hier ist ok")
            except Exception as e: 
                error = "Something went wrong while inserting the data into tbl_demand"
                print(error)
                print(e)
                return render_template('signup.html', error=error)
     
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

@app.route('/showLogin',methods=['GET','POST'])
def showLogin():
    if request.method=='POST':
        details=request.form
        fName=details['fname']
        lName=details['lname']

        email='hallo'
        
        sql = "INSERT INTO users(username, password, email) VALUES (%s, %s, %s)"
        val=(fName, lName, email)
        
        cur=mydb.cursor()

        cur.execute(sql, val)
        mydb.commit()
        cur.close()
    
        return('success')
    
    return render_template('login.html') 

@app.route('/map')
def showMap():
    return render_template('map.html')

@app.route('/mapPoints') #retrieve map points in the database
def getMapPoints():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM tbl_institutions")

    myresult = mycursor.fetchall()
    payload = []
    content = {}
    for result in myresult:
       content = {'institutionid': result[0], 'name': result[1], 'type': result[2], 'address': result[3], 'contact': result[4], 'telephone': result[5], 'lat': result[6], 'lng': result[7]}
       payload.append(content)
       content = {}
    return jsonify(payload)

   # myresult = mycursor.fetchone() for just the first result
    # jsonResults = json.dumps(myresult)

  #  for x in myresult:
   #     print(x)
   # return ('test')

@app.route('/showProfile')
def showProfile():
    return render_template('profile.html')

@app.route('/deliveries')
def showDeliveries():
    username = request.args.get('username')
    print(username)
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



if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=5000)
    app.run(port=5000)


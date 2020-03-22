from flask import Flask, render_template, json, request, url_for, redirect, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
import requests
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

app = Flask(__name__)
mydb = mysql.connector.connect(
        host="52.166.36.96",
        user="app",
        passwd="covid789", 
        database ="hackathon"
    )       

print(mydb)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/signup', methods=['GET', 'POST'])
def showSignUp():
    #bei Get soll er das nur rendern .. 
    if request.method=='POST': 
        
        details = request.form
        inputName = details['inputName']
        inputAddress= details['inputAdress']
        inputContact = details['inputAnsprechpartner']
        inputTelephone = details['inputTelephone']
        inputNeed = details['inputNeed']
        inputAnzahlNeed = details['inputAnzahlNeed']
        inputGive= details['inputGive']
        inputAnzahlGive = details['inputAnzahlGive']

       
        if details['inputInstitution'] == "Medizinische Einrichtung": 
            institutionType = "medical"
        elif details['inputInstitution'] == "Unternehmen": 
            institutionType =  "company"
        else: 
            institutionType="undefined"
        
   
        
        sql_institution = "INSERT INTO tbl_institutions (name, type, address, contact, telephone, lat, lng) VALUES(%s,%s,%s,%s,%s,%s.%s)"
        values_institution = (inputName, institutionType,inputAddress, inputContact, inputTelephone, 0.0, 0.0)

        print(sql_institution)
        print(values_institution)
        
        cur = mydb.cursor()
        try: 
            cur.execute(sql_institution, values_institution)
            mydb.commit()
            
            cur.execute( "Select last_insert_id()")
            inst_id = mydb.commit()

        except: 
            error = "Something went wrong while inserting the data into tbl_institution"
            print(error)
            return render_template('signup.html', error=error)
        
        #print(inst_id)
        return("ok")
        # objecttypes = [{"Desinfektionsmittel":"disinfectants"}, {"Masken" : "masks"}, {"Handschuhe": "gloves"}]

        # if inputNeed and inputAnzahlNeed: 
        #     for object in objecttypes: 
        #         for key in object: 
        #             if inputNeed == key:
        #                 objectypeDB = objecttypes['object']['key']
            

            
        #     sql_demand= "INSERT INTO tbl_demand(fk_institution, objecttype, amount) VALUES (%s, %s,%s)"

        #     values_demand=(inst_id, objectypeDB, inputAnzahlNeed )
        #     try: 
        #         cur.execute(sql_demand, values_demand)
        #         mydb.commit()
        #     except: 
        #         error = "Something went wrong while inserting the data into tbl_demand"
        #         return render_template('signup.html', error=error)
        
        # return redirect("/map")


        #setzen der variablen
        #generate sql und execute - für die institution
        # generelt dann demand 
        # fehler abfangen - if fehler dann error zurück 
        # if no fehler -- redirect--auf map.html 

    

    elif request.method=='GET':
        return render_template('signup.html')

@app.route('/showLogin',methods=['GET','POST'])
def showLogin():
    if request.method=='POST':
        details=request.form
        fName=details['fname']
        lName=details['lname']
        
        
        sql = "INSERT INTO users(fname, lname) VALUES (%s, %s)"
        val=(fName, lName)
        
        cur=mydb.cursor()
        #cur.execute("INSERT INTO users(fname, lname) VALUES (%s, %s,%s)",(fName,lName,email))
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

@app.route('/showDeliveries')
def showDeliveries():
    return render_template('deliveries.html')

@app.route('/signup',methods=['POST','GET'])
def signUp():
    return('test')

if __name__ == "__main__":
    app.run(port=5000)


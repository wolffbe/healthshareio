from flask import Flask, render_template, json, request, url_for, redirect, flash, jsonify

from werkzeug.security import generate_password_hash, check_password_hash
import requests
import mysql.connector

from flask_cors import CORS, cross_origin

app = Flask(__name__)

cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

mydb = mysql.connector.connect(
       host="52.166.36.96",
        user="app",
        passwd="covid789", 
        database ="hackathon"
    ) #connect to our Azure DB

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignUp')
def showSignUp():
    return render_template('signup.html')

@app.route('/showLogin')
def showLogin():
    return render_template('login.html')

@app.route('/showMap')
def showMap():
    return render_template('map.html')

@app.route('/showProfile')
def showProfile():
    return render_template('profile.html')

@app.route('/showDeliveries')
def showDeliveries():
    return render_template('deliveries.html')

@app.route('/signup',methods=['POST','GET'])
def signUp():
    return('test')

@app.route('/mapPoints') #retrieve map points in the database
def getMapPoints():
    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM tbl_institutions") #Mquery MySQLDB

    myresult = mycursor.fetchall() 
    payload = []
    content = {}
    for result in myresult: #create content for JSON
       content = {'institutionid': result[0], 'name': result[1], 'type': result[2], 'address': result[3], 'contact': result[4], 'telephone': result[5], 'lat': result[6], 'lng': result[7]}
       payload.append(content)
       content = {}
    return jsonify(payload)


if __name__ == "__main__":
    app.run(port=5000)
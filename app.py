from flask import Flask, render_template, json, request
from flaskext.mysql import MySQL
from werkzeug.security import generate_password_hash, check_password_hash
import requests
from flask_restful import Resource, Api
from flask_cors import CORS
import requests

mysql = MySQL()
app = Flask(__name__)
app.config["DEBUG"] = True
CORS(app)

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

if __name__ == "__main__":
    app.run(port=5000)
from flask import Flask, render_template, json, request

from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)



@app.route('/')
def main():
    return render_template('index.html')

@app.route('/showSignup')
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

if __name__ == "__main__":
    app.run(port=5000)
from flask import Flask, request, session
from flask import render_template, url_for, redirect
import csv

class User:
    def __init__(self, email):
        self.email = email
    

class Times:
    def __init__(self, monS, tueS, wedS, thuS, friS, satS, sunS, monE, tueE, wedE, thuE, friE, satE, sunE):
        self.monS = monS
        self.tueS = tueS
        self.wedS = wedS
        self.thuS = thuS
        self.friS = friS
        self.satS = satS
        self.sunS = sunS
        self.monE = monE
        self.tueE = tueE
        self.wedE = wedE
        self.thuE = thuE
        self.friE = friE
        self.satE = satE
        self.sunE = sunE

users = []
names = {}
idx = 0

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")


@app.route("/scripts/index")
def scriptind():
    return render_template("/scripts/index.js")


@app.route("/scripts/init-fire")
def scriptinitfire():
    return render_template("/scripts/init-firebase.js")


@app.route("/scripts/home")
def scripthome():
    return render_template("/scripts/home.js")


@app.route("/scripts/signUp")
def scriptsignup():
    return render_template("/scripts/signUp.js")

@app.route("/styles/main")
def mainstyle():
    return render_template("/styles/main.css")

@app.route("/successful", methods=["POST"])
def successful():
    login_user = User(request.form["email"])
    users.append(login_user)
    return render_template("user/index.html")

@app.route("/home", methods=["POST"])
def home():
    rows = [request.form["monS"], request.form["monE"],
            request.form["tueS"], request.form["tueE"],
            request.form["wedS"], request.form["wedE"],
            request.form["thuS"], request.form["thuE"],
            request.form["friS"], request.form["friE"],
            request.form["satS"], request.form["satE"],
            request.form["sunS"], request.form["sunE"]]
    
    with open("new_file.csv", "a") as f:
        ruleswriter = csv.writer(f)
        ruleswriter.writerow([row for row in rows])

    return render_template("user/index.html")

@app.route("/userSignUp")
def userSignUp():
    return render_template("/user/signUp.html")


@app.route("/availability", methods=["POST"])
def availability():
    with open("new_file.csv", "a") as f:
        ruleswriter = csv.writer(f)
        ruleswriter.writerow([request.form["name"]])
    return render_template("/user/availability.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/orgLogin")
def orgLogin():
    return render_template("/organizer/orgLogin.html")

@app.route("/orgOpenTime")
def orgOpenTime():
    return render_template("/organizer/orgOpenTime.html")

@app.route("/orgSignUp")
def orgSignUp():
    return render_template("/organizer/orgSignUp.html")

@app.route("/orgUserInfo")
def orgUserInfo():
    return render_template("/organizer/orgUserInfo.html")  

@app.route("/logout")
def logout():
    return render_template("/logout.html")  

app.run()

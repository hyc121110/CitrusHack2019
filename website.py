from flask import Flask, request
from flask import render_template

class User:
    def __init__(self, email, password):
        self.email = email


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


@app.route("/successful", methods=["POST"])
def successful():
    login_user = User(request.form["email"], request.form["password"])
    print(login_user.email)
    return render_template("user/index.html")


@app.route("/orgLogin")
def orgLogin():
    return render_template("/organizer/orgLogin.html")


@app.route("/userSignUp")
def userSignUp():
    return render_template("/user/signUp.html")

@app.route("/schedule")
def schedule():
    return render_template("schedule.html")

@app.route("/orgOpenTime")
def orgOpenTime():
    return render_template("/organizer/orgOpenTime.html")    

@app.route("/orgUserInfo")
def orgUserInfo():
    return render_template("/organizer/orgUserInfo.html")  

@app.route("/logout")
def logout():
    return render_template("/logout.html")  

app.run()

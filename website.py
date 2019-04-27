from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("index.html")


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

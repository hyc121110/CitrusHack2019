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

app.run()

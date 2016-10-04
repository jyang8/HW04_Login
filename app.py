from flask import Flask, render_template, request
from utils import datacheck

app = Flask(__name__)

@app.route("/")
@app.route("/login/")
def tmplt():
    return render_template("login.html")

@app.route("/authenticate/", methods=["POST"])
def auth():
    users = datacheck.getDict()
    un = request.form["user"]
    pw = datacheck.hashPW( request.form["password"] )
    
    if request.form["button"] == "Login": #Login
        if not un in users.keys():
            msg = "User does not exist!"
        elif (users[un] != pw):
            msg = "Wrong password!"
        else:
            msg = "You're in!"
    else: #Register
        if un in users.keys():
            msg = "User already exists!"
        else:
            datacheck.addEntry(un,pw)
            msg = "Good to go!"
    return render_template( "result.html", resultmsg = msg )

if __name__ == "__main__":
    app.debug = True
    app.run()


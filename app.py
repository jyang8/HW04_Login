from flask import Flask, render_template, request, session, url_for, redirect
from utils import datacheck

app = Flask(__name__)
app.secret_key = '\xfa\\\xda$\\\x06\xdd2mI\xed\x9bW\xa8A\xa6\x86l\xcd\xe4\xa9L\xf9L\xa8>\xe3 \x05\xf2p\xeb'

@app.route("/")
@app.route("/login/")
def login():
    if "username" in session: #logged in
        return redirect( url_for("welcome") )
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
            msg = ""
            session["username"] = un
            return redirect( url_for("welcome") )
    else: #Register
        if un in users.keys():
            msg = "User already exists!"
        else:
            datacheck.addEntry(un,pw)
            msg = "Good to go!"
    return render_template( "login.html", resultmsg = msg )

@app.route("/welcome/")
def welcome():
    return render_template("welcome.html")

@app.route("/logout/", methods=["POST"])
def logout():
    if request.form["button"] == "Log Out": #LogOut
        session.pop("username")
        return redirect( url_for("goodbye") )

@app.route("/goodbye/")
def goodbye():
    return "Goodbye. <a href=\"..\login\">Login?</a>"

if __name__ == "__main__":
    app.debug = True
    app.run()


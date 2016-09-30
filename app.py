from flask import Flask, render_template, request

app = Flask(__name__)
users = {"DW":"work04"}

@app.route("/")
@app.route("/login/")
def tmplt():
    return render_template("login.html")

@app.route("/authenticate/", methods=["POST"])
def auth():
    for name in users:
        if name == request.form["user"]:
            if users.get(name) == request.form["password"]:
                return render_template("result.html", result="Success!! :)", resultmsg="You're in!!")
            else:
                return render_template("result.html", result="Failure!! :(", resultmsg="Wrong password. Try again!!")
        else:
            return render_template("result.html", result="Failure!! :(", resultmsg="User does not exist.")

if __name__ == "__main__":
    app.debug = True
    app.run()


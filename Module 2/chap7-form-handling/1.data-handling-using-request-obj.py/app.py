from flask import Flask, render_template
from flask import request
app = Flask(__name__)

users = {
    "archie.andrews@email.com": "football4life",
    "veronica.lodge@email.com": "fashiondiva"
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        if email in users and users[email] == password:
            return render_template("login.html", message ="Successfully Logged In")
        return render_template("login.html", message ="Incorrect Email or Password")
    return render_template("login.html")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
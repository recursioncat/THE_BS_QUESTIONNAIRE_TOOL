from flask import Flask, redirect, render_template

app = Flask(__name__)

@app.route("/")
def main():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("main.html")

app.run(debug=True)
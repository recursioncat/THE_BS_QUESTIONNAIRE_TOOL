from flask import Flask, redirect, render_template, request, session, send_from_directory
from Server.randomstring import genString
from Server.JSONParser import makeQuestionnaire
import os
import shutil

app = Flask(__name__)
app.secret_key = os.environ.get('Flask_Secret_key')
list_of_Users = []

@app.route("/")
def main():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("Homepage.html")

@app.route("/new-questionnaire", methods = ['GET'])
def newRoom():
    id = genString(20)
    while id in list_of_Users:
        id = genString(20)

    session["id"] = id
    os.mkdir(f"users/{id}")
    list_of_Users.append(id)

    session["path"] = f'Users/{id}'
    shutil.copytree('HTML MAPPER', session["path"], dirs_exist_ok=True)
    return render_template('main.html')


@app.route("/process-questionnaire", methods=['POST'])
def processQuestionnaire():
    # try: 
    data = request.form['data']
    makeQuestionnaire(data)
    return render_template("DownloadReady.html", path = session["path"])

    # except Exception as e:
    #     return str(e)
    
@app.route('/Users/<path:filename>')
def serve_user_file(filename):
    return send_from_directory('Users', filename)


if __name__=="__main__":
    app.run(debug=True)
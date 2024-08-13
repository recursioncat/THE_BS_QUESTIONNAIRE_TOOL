from flask import Flask, redirect, render_template, request, session, send_from_directory, flash, url_for
from Server.randomstring import genString
from Server.JSONParser import makeQuestionnaire
import os
import shutil

app = Flask(__name__)
app.secret_key = os.environ.get('Flask_Secret_key')
list_of_Users = ['testusername260704Rishit']

@app.route("/")
def main():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("Homepage.html")

@app.route('/feedback')
def feedback():
    return render_template('feedback.html')

@app.route('/docs')
def docs():
    return render_template('docs.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/new-questionnaire", methods = ['POST'])
def newRoom():
    id = request.form.get('Username')
    if id in list_of_Users:
        flash('Please Enter Another Username\nWhat are the Chances!\nSomeone else is using that username')
        return redirect(url_for('.home'))
    
    if len(id) < 5:
        flash('Whoops! Please enter an username at least 5 characters long.')
        return redirect(url_for('.home'))

    if len(id) > 20:
        flash('Whoops! Please enter an username within 20 characters.')
        return redirect(url_for('.home'))

    session["id"] = id
    if not os.path.isdir(f"users/{id}"):
        os.mkdir(f"users/{id}")
        list_of_Users.append(id)

    session["path"] = f'Users/{id}'
    print(f"NEW USER: {id},\nPATH: {session['path']}")

    shutil.copytree('HTML MAPPER', session["path"], dirs_exist_ok=True)
    return render_template('main.html')


@app.route("/process-questionnaire", methods=['POST'])
def processQuestionnaire():
    try: 
        data = request.form['data']
        makeQuestionnaire(data)
        # return render_template("DownloadReady.html", path = session["path"])
        return render_template("DownloadReady.html", path = 'Users/RishitChakraborty')

    except Exception as e:
        return str(e)
    
@app.route('/Users/<path:filename>')
def serve_user_file(filename):
    return send_from_directory('Users', filename)


if __name__=="__main__":
    app.run(debug=True)
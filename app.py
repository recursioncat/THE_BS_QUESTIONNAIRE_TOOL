from flask import Flask, redirect, render_template, request, json
from Server.questionnaire1 import Question


app = Flask(__name__)

@app.route("/")
def main():
    return redirect("/home")

@app.route("/home")
def home():
    return render_template("main.html")


@app.route("/process-questionnaire", methods=['POST'])
def processQuestionnaire():
    data = request.form['data']
    questionnaire = json.loads(data)
    nums = questionnaire["amount"]


    listOfQuestions = []
    for i, question in enumerate(questionnaire["questions"]):
        option_list = []
        option_value = []
        options = question["optionList"]
        for option in options:
            option_list.append(option["text"])
            option_value.append(option["value"])

        obj = Question(i+1, question["text"], option_list, option_value, 10)
        print("weightList: ")
        obj.weights.show()
        listOfQuestions.append(obj)

    for i in range(10):
        print(questionnaire["title"])
        for question in listOfQuestions:
            print(question.questionNumber, " ", end="")
            print(question.questionText)

            for i, option in enumerate(question.optionsList):
                print("\t", i+1, ". ", end = "")
                print("\t", option, end = "")

                if i == question.weights.top():
                    print(" (Ans)")
                else:
                    print()

            question.weights.pop()

    
    return "SUCCESS"

app.run(debug=True)
import json
from .mapper import *
from .questionnaire1 import Question
from flask import session
from.grapher import graphOut

def parse(JSONFile):
    try:
        print("inside Parse Function")
        questionnaire = json.loads(JSONFile)
        print(questionnaire)
        nums = questionnaire["amount"]
        listOfQuestions = []
        for i, question in enumerate(questionnaire["questions"]):
            
            option_list = [] # --> Contains the Text in Each Option
            option_value = [] # --> Contains the Weightage of each option

            options = question["optionList"]
            
            for option in options:
                option_list.append(option["text"])
                option_value.append(option["value"])

            
            #Handle Questions with Particular algo
            valueforcheckedQuestions = [0 for i in range(len(options))]         
            if question["algo"] == "Perticular":
                for i, _ in enumerate(options):
                    if options[i]["check"] == True:
                        valueforcheckedQuestions[i] = 1
                        break
                option_value = valueforcheckedQuestions 

            obj = Question(i+1, question["type"],  question["text"], option_list, option_value, 10, question["algo"])
            
            listOfQuestions.append(obj)
            
        print("This is the Recieved Path: ", session['path'])
        HTMLMapper = Mapper(str(session['path'])+'/output.html')
        
        for i in range(10): # --> Hook up to nums later/ Writes Each Questionnaire this many times

            HTMLMapper.add_heading(questionnaire['title'])
            for question in listOfQuestions:
                textBody = str(question.questionNumber) + ". " + question.questionText
                if question.type == "MCQ":
                    listOfOptions = []
                    for option in question.optionsList:
                        listOfOptions.append(str(option))
                    ques = HTMLQuestion(textBody, listOfOptions, question.weights.top())
                    HTMLMapper.add_question(ques)

                    graphOut(option_list, obj.weightList, session["path"], True, question.questionNumber, question.questionText)
    
                    question.weights.pop()
                    print(question.weights)
                    
                elif question.type == 'Open-Ended':
                    HTMLMapper.add_open_ended_question(textBody)
            
            HTMLMapper.insert_page_break()

        HTMLMapper.add_heading("Data")
        for i in range(1, len(listOfQuestions)+1):
            if listOfQuestions[i-1].type != 'Open-Ended':
                HTMLMapper.add_graph(str(i)+".png")
        
        HTMLMapper.close()

    except Exception as e:
        raise e
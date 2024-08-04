import json
from .questionClass import Question
from .OpenEndedQuestionClass import OpenEndedQuestion

def parse(jsonData):
    data = json.loads(jsonData)
   #  print(data['amount'])
    listOfQuestions = []
    for i, question in enumerate(data['questions']):
        if question['type'] == 'Open-Ended':
            listOfQuestions.append(OpenEndedQuestion(i, question['text']))
        else:
            print("optionLIst: ", question['optionList'])

            #change 10
            QuestionObject = Question(i+1, question['text'], question['algo'], question['optionList'], int(data['amount']))
            listOfQuestions.append(QuestionObject)
    
    return listOfQuestions






if __name__ == "__main__":
   # # print(parse('''
   # {
   #    "amount":"100",
   #    "title":"Let's Talk About the Beatles",
   #    "detail":"Lorem ipsum dolor sit amet consectetur adipisicing elit Minima corrupti ducimus aliquid.",
   #    "questions":[
   #       {
   #          "text":"Who is your favorite Beatle",
   #          "type":"MCQ",
   #          "algo":"Random",
   #          "optionList":[
   #             {
   #                "check":false,
   #                "text":"John",
   #                "value":0
   #             },
   #             {
   #                "check":false,
   #                "text":"Paul",
   #                "value":0
   #             },
   #             {
   #                "check":false,
   #                "text":"George",
   #                "value":0
   #             },
   #             {
   #                "check":false,
   #                "text":"Ringo",
   #                "value":0
   #             }
   #          ]
   #       },
   #       {
   #          "text":"If i needed someone to...",
   #          "type":"MCQ",
   #          "algo":"Perticular",
   #          "optionList":[
   #             {
   #                "check":true,
   #                "text":"Love",
   #                "value":0
   #             },
   #             {
   #                "check":false,
   #                "text":"Beat",
   #                "value":0
   #             },
   #             {
   #                "check":false,
   #                "text":"Eat",
   #                "value":0
   #             }
   #          ]
   #       },
   #       {
   #          "text":"Tell us about your favorite song",
   #          "type":"Open-Ended",
   #          "algo":"Random",
   #          "optionList":[
               
   #          ]
   #       },
   #       {
   #          "text":"What is your favorite Album?",
   #          "type":"MCQ",
   #          "algo":"Custom",
   #          "optionList":[
   #             {
   #                "check":false,
   #                "text":"Rubber Soul",
   #                "value":0.1
   #             },
   #             {
   #                "check":false,
   #                "text":"Abbey Road",
   #                "value":0.4
   #             },
   #             {
   #                "check":false,
   #                "text":"Let it Be",
   #                "value":0.3
   #             },
   #             {
   #                "check":false,
   #                "text":"Revolver",
   #                "value":0.05
   #             },
   #             {
   #                "check":false,
   #                "text":"White Album",
   #                "value":0.1
   #             },
   #             {
   #                "check":false,
   #                "text":"Sgt Pepper",
   #                "value":0.05
   #             }
   #          ]
   #       }
   #    ]
   # }
   # '''))
   pass
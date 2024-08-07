from .QuestionnaireParser import parse
from flask import session
import json
from .mapper import *
from .grapher import graphOut

def makeQuestionnaire(jsonFile:str):
    data = json.loads(jsonFile)
    print(data)
    title = data['title']
    itterations = int(data['amount'])
    ShowSubHeading = data['subhead']
    ShowGraphs = data['graphs']
    GraphType = data['grapht']
    subHeadingText = data['detail']

    listOfQuestions = parse(jsonFile)
    # HTMLMapper = Mapper("Server"+"/"+"output.html")
    HTMLMapper = Mapper(session['path']+"/"+"output.html")
    question_numbers_with_graph = []
    
    # Questions
    for i in range(itterations): #change
        HTMLMapper.add_heading(title)
        if(ShowSubHeading):
           HTMLMapper.add_subheading(subHeadingText)
        for question in listOfQuestions:

            if question.type == 'MCQ':
                list_of_options = [i for _,i in question.options]
                list_of_option_values = question.option_temp

                # print("Here are em Options: ",question.options)
                # print("Here is what we got: ", list_of_options, "and", list_of_option_values )

                Ques = HTMLQuestion(str(question.number)+ '.' + question.text, list_of_options, question.weightlist.top())
                question.weightlist.pop()
                HTMLMapper.add_question(Ques)
               
                if (ShowGraphs):
                  graphOut(list_of_options, list_of_option_values,session['path'], True, question.number, question.text, GraphType)
                  if i == 0:
                     question_numbers_with_graph.append(question.number)


            elif question.type == 'Open-Ended':
                HTMLMapper.add_open_ended_question(str(question.number)+ '.' + question.text)
            
            else:
                raise Exception("Question Type Not Understood, Question passed was neither MCQ nor Open-Ended")
        
        HTMLMapper.insert_page_break()
    

    #Graphs
    if (ShowGraphs):
      HTMLMapper.add_heading("Graphs/Data")
      for question_number in question_numbers_with_graph:
         HTMLMapper.add_graph(str(question_number)+'.png')


    HTMLMapper.close()


if __name__ == "__main__":
    makeQuestionnaire('''
    {
   "amount":"100",
   "title":"Let's Talk About the Beatles",
   "detail":"Lorem ipsum dolor sit amet consectetur adipisicing elit Minima corrupti ducimus aliquid.",
   "questions":[
      {
         "text":"Who is your favorite Beatle",
         "type":"MCQ",
         "algo":"Random",
         "optionList":[
            {
               "check":false,
               "text":"John",
               "value":0
            },
            {
               "check":false,
               "text":"Paul",
               "value":0
            },
            {
               "check":false,
               "text":"George",
               "value":0
            },
            {
               "check":false,
               "text":"Ringo",
               "value":0
            }
         ]
      },
      {
         "text":"If i needed someone to...",
         "type":"MCQ",
         "algo":"Perticular",
         "optionList":[
            {
               "check":true,
               "text":"Love",
               "value":0
            },
            {
               "check":false,
               "text":"Beat",
               "value":0
            },
            {
               "check":false,
               "text":"Eat",
               "value":0
            }
         ]
      },
      {
         "text":"Tell us about your favorite song",
         "type":"Open-Ended",
         "algo":"Random",
         "optionList":[
            
         ]
      },
      {
         "text":"What is your favorite Album?",
         "type":"MCQ",
         "algo":"Custom",
         "optionList":[
            {
               "check":false,
               "text":"Rubber Soul",
               "value":0.1
            },
            {
               "check":false,
               "text":"Abbey Road",
               "value":0.4
            },
            {
               "check":false,
               "text":"Let it Be",
               "value":0.3
            },
            {
               "check":false,
               "text":"Revolver",
               "value":0.05
            },
            {
               "check":false,
               "text":"White Album",
               "value":0.1
            },
            {
               "check":false,
               "text":"Sgt Pepper",
               "value":0.05
            }
         ]
      }
   ]
}
''')

    pass




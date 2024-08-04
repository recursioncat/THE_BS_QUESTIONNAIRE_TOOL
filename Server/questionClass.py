from .stack import stack
from .randomgen import WeightedRandom
from .optionClass import Option
import json

class Question:
    def __init__(self, number, text, algorithm, optionList, iterations) -> None:
        self.number = number
        self.text = text
        self.algorithm = algorithm
        self.type = "MCQ"

        self.options = [(i, option['text']) for i, option in enumerate(optionList)]

        self.option_temp = Option(optionList, algorithm).getValue()
        print(self.option_temp)
        self.weightlist = stack(WeightedRandom(self.option_temp, iterations))

    def getWeights(self):
        return self.weightlist
    
    def ShowSelf(self):
        print(f'''
        Qustion Number : {self.number}
        Question Text : {self.text}
        Question Algorithm: {self.algorithm}
        Question Options: {self.options}
        Option Weights ; {self.option_temp}
        Question Weightlist : {self.weightlist.showWhole()}
''')
        

if __name__ == "__main__":
#     optionList = json.loads('''[
#             {
#                "check":true,
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
#          ]''')
    
#     QuesObj = Question(1, "Who is your favorite Beatle", "Perticular", optionList, 10 )
#     QuesObj.ShowSelf()

#     print(len(optionList))

   pass
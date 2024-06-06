import pickle
import random

class Questionnaire:
    def __init__(self, name=None, list_of_questions=None, filename = None):
        if filename == None:
            self.name = name
            self.list_of_questions = list_of_questions
        else:
             with open(filename, 'rb') as f:
                var = pickle.load(f)
        
                self.name = var.name
                self.list_of_questions = var.list_of_questions

    def show_questions(self):
        for question in self.list_of_questions:
            question.show_self()

 
def make_questionnaire(instance:Questionnaire):
    with open(instance.name+".ques", 'wb') as f:
        pickle.dump(instance, f)          

class Question:
    def __init__(self, Question_text, type) -> None:
        self.question = Question_text
        self.type = type
        self.options = []
        self.number_of_options = len(self.options)

    def define_option(self, option):
        self.options.append(Option(option))
        self.number_of_options = len(self.options)

    def define_distribution(self, choice=None, choice_list = None, type = "normal" ):


        if type == "normal":
            on_option = self.options[choice-1]
            on_option.percentage = 100

            for choice in self.options:
                if choice!=on_option:
                    choice.percentage = 0


        if type == "random":
            temp =[]
            for i in range(self.number_of_options):
                val = random.randint(0,11)
                temp.append(val)
            su = sum(temp)

            for i, value in enumerate(temp):
                temp[i] = round(value/su*100, 1)

            for i, _ in enumerate(self.options):
                self.options[i].percentage = temp[i]  


        if type == "list-based":
            if sum(choice_list)!=100:
                print("The Total isn't 100")
                return

            print(len(choice_list))
            print(len(self.options))

            for i, _ in enumerate(choice_list):
                self.options[i].percentage = choice_list[i]
            
                



    
    def show_options(self):
        for option in self.options:
            print(f"{option.value}: {option.percentage}")
    
    def show_self(self):
        print(self.question)
        for i in self.options:
            print(f" {i.value}: {i.percentage}")
        print("\n")
        

class Option:
    def __init__(self,option_text, answer_percent=0) -> None:
        self.value = option_text
        self.percentage = answer_percent





one = Question("WW2 who win?", "checkbox")
one.define_option("hitler")
one.define_option("musso")
one.define_option("JAp")
one.define_option("merica")

one.define_distribution(4)


two = Question("WW1 who win?", "checkbox")
two.define_option("moto")
two.define_option("kekeo")
two.define_option("yolo")
two.define_option("rnad")
two.define_distribution(type="random")

three = Question("Who eat wood?", "checkbox")
three.define_option("Termi")
three.define_option("bee")
three.define_option("man")
three.define_option("horse")
three.define_distribution(choice=0, type="list-based", choice_list=[90,3,5,2])

    
ques = Questionnaire("hello", [one, two, three])
ques.show_questions()

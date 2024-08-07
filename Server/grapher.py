import matplotlib.pyplot as plt


def graphOut(optionTexts:list, optionValues:list, pathToSave:str, legend:str, questionNumber, questionText, type):
    
    plt.title(questionText)
    print("option Values form graph :", optionValues)

    if type == 'Pie':
        if legend == True:
            plt.pie(optionValues, autopct="%1.2f%%")
            plt.legend(optionTexts, loc="lower left", bbox_to_anchor = (1,0))
        
        elif legend == False:
            plt.pie(optionValues, labels=optionTexts, autopct="%1.2f%%")

        elif legend == "Both":
            plt.pie(optionValues, labels=optionTexts, autopct="%1.2f%%")
            plt.legend(optionTexts, loc="lower left", bbox_to_anchor = (1,0))

    elif type == 'Bar':
        plt.bar(optionTexts, optionValues)

    plt.savefig(f"{pathToSave}/{questionNumber}.png")
    plt.close() 


if __name__ == "__main__":
     listOfGraphs = [
          [["John", "George", "Paul", "Ringo"], [0.1, 0.2, 0.3, 0.4], 'Server', True, 1, "Question 1"],
          [["Hurt", "love", "me", "be"], [0, 1, 0, 0], 'Server', True, 2, "Question 2"],
          [["Rubber Soul", "White Album", "Let it Be", "Abbey Road", "Revolver"], [0.3, 0.3, 0.1, 0.1, 0.2], 'Server', True, 3, 'Question 3'],
     ]

     for option in listOfGraphs:
          graphOut(option[0], option[1], option[2], option[3], option[4], option[5],'Bar' )
import matplotlib.pyplot as plt

def graphOut(optionTexts:list, optionValues:list, pathToSave:str, legend:str, questionNumber, questionText):
    
    plt.title(questionText)

    if legend == True:
        plt.pie(optionValues, autopct="%1.2f%%")
        plt.legend(optionTexts, loc="lower left", bbox_to_anchor = (1,0))
    
    elif legend == False:
        plt.pie(optionValues, labels=optionTexts, autopct="%1.2f%%")

    elif legend == "Both":
           plt.pie(optionValues, labels=optionTexts, autopct="%1.2f%%")
           plt.legend(optionTexts, loc="lower left", bbox_to_anchor = (1,0))

    plt.savefig(f"{pathToSave}/{questionNumber}.png")

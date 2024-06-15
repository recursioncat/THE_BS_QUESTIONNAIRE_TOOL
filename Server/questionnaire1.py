from .stack import stack
from .randomgen import WeightedRandom

# Make questions from json and add em into list then iterate over them to write docx file

class Question:
    def __init__(self, questionNumber, questionText, optionsList, weightList, copies) -> None:
        self.questionNumber = questionNumber
        self.questionText = questionText
        self.optionsList = optionsList
        self.weightList = weightList
        self.copies = copies
        self.weights = stack(WeightedRandom(weightList, copies))

    def showWeights(self):
        self.weights.show()


if __name__ == "__main__":
   one = Question(1, "Who Won World War 2?", ['Adolf', 'Musso', "Mericans"], [0.2, 0.2, 0.6], 10)
   one.showWeights()
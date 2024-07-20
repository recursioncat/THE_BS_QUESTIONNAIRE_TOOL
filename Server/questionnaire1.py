from .stack import stack
from .randomgen import WeightedRandom, randomOfOne

# Make questions from json and add em into list then iterate over them to write docx file
class UnknownError(Exception):
    pass


class Question:
    def __init__(self, questionNumber, type, questionText, optionsList, weightList, copies, algo) -> None:
        self.type = type
        self.algo = algo
        if self.type == "Open-Ended":
            self.algo = None
        self.questionNumber = questionNumber
        self.questionText = questionText
        self.optionsList = optionsList
        self.weightList = weightList
        self.copies = copies
        if (self.type != 'Open-Ended'):
            if self.algo in ["Custom", "Perticular"]:
                self.weights = stack(WeightedRandom(self.weightList, self.copies))
            elif self.algo == "Random":
                self.weightList = randomOfOne(len(self.optionsList))
                self.weights = stack(WeightedRandom(self.weightList, self.copies))
            else:
                raise UnknownError("The Algo was not in the list of accepted algos")
        else:
            self.weights = stack([None])

    def showWeights(self):
        self.weights.show()


if __name__ == "__main__":
   
   one = Question(1, "Who Won World War 2?", ['Adolf', 'Musso', "Mericans"], [0.2, 0.2, 0.6], 10)
   print(one.type)
   one.showWeights()
from .randomgen import randomOfOne

class Option:
    def __init__(self, optionlist, algo) -> None:
        self.valueList = []
        if algo == "Perticular":
            for option in optionlist:
                self.valueList.append(1) if option['check'] == True else self.valueList.append(0)
        
        elif algo == 'Random':
            print("This is the len i am getting: ", len(optionlist))
            self.valueList = randomOfOne(len(optionlist))
        
        elif algo == 'Custom':
            for option in optionlist:
                self.valueList.append(option['value'])
        
        else:
            raise Exception("Unknown Algorithm Passed")

    def getValue(self):
        print("Option: ", self.valueList)
        return self.valueList
    

if __name__ == "__main__":
    randomOfOne(4)
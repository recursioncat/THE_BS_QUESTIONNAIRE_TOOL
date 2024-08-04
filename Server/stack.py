class emptyStack(Exception):
    pass


class stack:
    def __init__(self, data:list) -> None:
        if len(data)==0:
            raise emptyStack
        self.data = data[::-1]

    def push(self, value):
        self.data.append(value)
    
    def top(self):
        return self.data[-1]
    
    def pop(self):
        del self.data[-1]

    def show(self):
        print(self.data[::-1])

    def showWhole(self):
        return self.data
        

class OpenEndedQuestion:
    def __init__(self, number, text) -> None:
        self.number = number
        self.text = text
        self.type = 'Open-Ended'

    def ShowSelf(self):
        print(f'''
        Question Number: {self.number}
        Question Text: {self.text}
''')
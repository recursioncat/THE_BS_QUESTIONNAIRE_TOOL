class HTMLQuestion:
    def __init__(self, text, list_of_options, answer_index):
        self.text = text
        self.list_of_options = list_of_options
        self.answer_index = answer_index

    def get_html(self):
        ques = '<div class="question-section avoid-break">\n'
        ques += f'<p class="question">{self.text}</p>\n'
        options = '<div class="options-container">\n'

        for i, option in enumerate(self.list_of_options):
            if i == self.answer_index:
                options += f"""
                <div class="single-option">
                    <input type="checkbox">
                    <p class="option">{option}</p>
                    <img src="Ticks/5.png" class="tick">
                </div>\n
                """
            else:
                options += f"""
                <div class="single-option">
                    <input type="checkbox">
                    <p class="option">{option}</p>
                </div>\n
                """

        options += '</div>\n'
        ques += options
        ques += '</div>\n'

        return ques
    


class Mapper:
    def __init__(self, path) -> None:
        self.path = path
        self.file = open(path, 'a+')

        #copy js and css files to folder

        self.file.write("""
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <link rel="stylesheet" href="page.css">
                <script src="main.js" defer></script>
                <title>Document</title>
            </head>
            <body>
        """)

    def close(self):
        self.file.write("""
            </body>
            </html>
        """)

        self.file.close
        print("Mapper File Closed.")
    
    def add_question(self, question: HTMLQuestion):
        self.file.write(question.get_html())

    def add_open_ended_question(self, questionText):
        ques = '<div class="question-section avoid-break">\n'
        ques += f'<p class="question">{questionText}</p>\n'
        ques += f'<br><br><br><br><br>\n'
        ques += '</div>\n'
        self.file.write(ques)
        

    def add_heading(self, text):
        self.file.write(f"<h1>{text}</h1>\n")

    def add_subheading(self, text):
        self.file.write(f"<h2>{text}</h2>\n")

    def insert_page_break(self):
        self.file.write('<div class="page-break"></div>\n')

    def add_graph(self, question_number):
        self.file.write(f''' 
            <div class="graph-container avoid-break">
                <img class="graph" src="{question_number}">
            </div>\n
        ''')
        

if __name__ == "__main__":

    mapper = Mapper('output.html')

    q1 = HTMLQuestion("1. Who Started World War 1?", ["Hitler", "Gandhi", "Mussolini", "Mericans"], 0)
    q2 = HTMLQuestion("2. What is the Best Beatles Album?", ["Revolver", "Abbey Road", "Rubber Soul", "White Album"], 2)

    mapper.add_heading("Helllo")
    mapper.add_question(q1)
    mapper.insert_page_break()
    mapper.add_question(q2)



    mapper.close()


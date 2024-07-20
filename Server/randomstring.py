import random

def genString(len):
    allowedChars = 'abcdefghijklmnopqrstuvwxyz1234567890$-()+!'
    id = ''
    for i in range(len):
        choice = random.choice(allowedChars)
        id += choice
    
    return id

if __name__ == "__main__":
    print(genString(20))
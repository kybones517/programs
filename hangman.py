import random as r

print("Welcome to Ky's Hangman Game2.0!")
print("Please Think of a word that isn't a proper noun,\n and doesn't contain any numbers or letters")
correct = 0
clue = []
attempts = 10
databank = []
for letter in range(97,122):
  databank.append(chr(letter))
 
def getWordLen():
  global clue
  print("Enter length of your word!")
  while(True):
    try:
      userInput = int(input(">>>: "))
    except ValueError:
      print("Invaild Input!")
    else:
    clue = list("*"userInput)
    print(clue)
    break
   
 
 

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
   
getWordLen()

while attempts > 0:
    guess = r.choice(databank)
    print("is the letter %s in your word?"% guess)
    anwser = input(">>>: ")
    if anwser == "y":
        correct +=1
        print("Found!")
        print("How many occurrences?")
        while(True):
            try:
                occur = int(input(">>>: "))
                #updateClue(int(input("Index: ")))
                for i in range(occur):
                    x = int(input("Index:"))
                    clue.remove(clue[x])
                    clue.insert(x,guess)
                
            except (ValueError,IndexError):
                print("invalid index")
            else:
                break
        print(clue)
    else:
        attempts-=1
        print(attempts)
    if correct == len(clue):
        print("I win!") 
        break
    databank.remove(guess)
    
    if attempts == 0:
      print("I have Lost! :(")
      print("You win!") 
    
 

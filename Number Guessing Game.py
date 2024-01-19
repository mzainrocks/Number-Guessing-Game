from random import randint

number = randint(1, 100)
GuessCount = 0
NumberGuessed = False
Guess = 0

print("Im Thinking Of A Number Between 1 And 100...")
print("Make A Guess And I'll Tell You Whether Its Higher Or Lower")

while NumberGuessed == False:
    Guess = int(input("Enter Your Guess"))
    GuessCount += 1
    if number > Guess:
        print ("Higher")
    elif number < Guess:
        print ("Lower")
    elif number == Guess:
        print ("Well Done! You Have Guessed The Number In " + str(GuessCount) + " Guesses!")
NumberGuessed = True

userName = input("Input your name: ")
print(f"Hello {userName}! Welcome to your daily math quiz! ")

from random import randint

def NumbGenerator():
    num1 = randint(0, 99)
    num2 = randint(0, 99)
    return num1,num2

NumberofRounds = 1
Score = 0

while NumberofRounds != 11:
    numA, numB = NumbGenerator()
    print(f"Game {NumberofRounds} will be started!\nGoodluck and have fun!\nYour current score status is {Score} out of 10")
    answerUser = int(input(f"Determine the sum of {numA} and {numB}?\n"))
    CorrectSum = numA + numB
    if CorrectSum == answerUser:
        NumberofRounds += 1
        Score += 1
    else:
        NumberofRounds += 1

def GameOver():
    print(f"Your overall score on this test is {Score}/10!\nThank you for playing! ")
GameOver()
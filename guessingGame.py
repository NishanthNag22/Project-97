import random
from typing import ChainMap

print("Number Guessing Game")

number=random.randint(1,9)
chances=0

print("Guess a number (Between 1 to 9)")

while chances < 5:

    guess=int(input("Enter Your Guess : "))

    if guess==number:
        print("CONGRATULATIONS YOU WON !!!")
        break
    elif(guess<number):
        print("Your guess is too low , Enter a number greater than ",guess)
    else:
        print("Your guess is too high , Enter a number lesser than ",guess)

    chances+=1

if not chances < 5:
    print("YOU LOSE !!! The number is ",number)
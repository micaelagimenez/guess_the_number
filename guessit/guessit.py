import random 
from random import randint

play = True

while play:
    n = random.randint(1,101)
    guess = int(input("Guess number between 1 to 100\n"))

    while n != 'guess':
        if guess > n:
           print("Guess is too high.")
           guess = int(input("Guess number between 1 to 100\n"))
        if guess < n:
           print("Guess it too low.")
           guess = int(input("Guess number between 1 to 100\n"))
        else:
           print("Correct")
           break

    answer = input("Play again?\n")
    if answer == "no":
        play = False
        print("Goodbye.")
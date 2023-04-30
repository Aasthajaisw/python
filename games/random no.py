
import random
n=random.randint(1,20)
name=input("Enter your name ")
print("Welcome " + name)
# No. of times you want to try
turns=int(input("Enter number of times you want to try "))
# Let's play the game
for i in range (turns):
    guess=int(input("Guess a number "))
    if guess==n:
        print("Congrats! You won")
        break
    elif guess<n:
        print("It is smaller than number")
    else:
        print("It is a larger number")

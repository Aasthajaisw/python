import random

def roll_dice():
    # generate a random number between 1 and 6
    return random.randint(1, 6)

print("Welcome to the dice game!")
n = int(input("Enter the no. of rounds you want to play: "))
player_score = 0
computer_score = 0

# play 5 rounds
for i in range(n):
    print(f"Round {i+1}:")
    # player's turn
    input("Press enter to roll the dice...")
    player_roll = roll_dice()
    print(f"You rolled a {player_roll}!")
    player_score += player_roll
    print(f"Your total score is {player_score}.")
    # computer's turn
    computer_roll = roll_dice()
    print(f"The computer rolled a {computer_roll}!")
    computer_score += computer_roll
    print(f"The computer's total score is {computer_score}.\n")

# determine the winner
print("Game over!")
if player_score > computer_score:
    print("Congratulations, you win!")
elif player_score < computer_score:
    print("Sorry, the computer wins.")
else:
    print("It's a tie!")

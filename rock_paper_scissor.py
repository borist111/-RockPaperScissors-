import random

scissor = "Scissors"
rock = "Rock"
paper = "Paper"

player_move = input("Choose [r]ock, [p]aper, or [s]cissors: ")

if player_move == "r":
    player_move = rock
elif player_move == "p":
    player_move = paper
elif player_move == "s":
    player_move = scissor
else:
    raise SystemExit("Invalid Input. Try again...")

computer_random_number = random.randint(1, 3)
computer_move = ""

if computer_random_number == 1:
    computer_move = rock
elif computer_random_number == 2:
    computer_move = paper
elif computer_random_number == 3:
    computer_move = scissor

print(f"The computer chose {computer_move}.")
print(f"You chose {player_move}.")

# Determine the winner
if player_move == computer_move:
    print("It's a tie!")
elif (player_move == rock and computer_move == scissor) or \
     (player_move == paper and computer_move == rock) or \
     (player_move == scissor and computer_move == paper):
    print("You win!")
else:
    print("You lose!")

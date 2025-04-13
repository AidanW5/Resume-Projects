#have user input rock, paper, or siccors and then use random generator for rock, paper, scissors

import random

Rps = ["Rock", "Paper", "Scissors"]

ai = random.choice(Rps)

user = input("Please enter Rock, Paper, or Scissors: ")

player_one = user.capitalize()

print("The computer picked: " + ai)

#Outcomes
if player_one == ai:
    print("It's a tie! You both chose "+ ai)

elif player_one == "Rock" and ai == "Paper":
    print("Paper beats Rock, you lost :(")

elif player_one == "Rock" and ai == "Scissors":
    print("Rock beats Scissors, you won! :)")

elif player_one == "Paper" and ai == "Rock":
    print("Paper beats Rock, you won! :)")
    
elif player_one == "Paper" and ai == "Scissors":
    print("Scissors beats Paper, you lost :(")
    
elif player_one == "Scissors" and ai == "Rock":
    print("Rock beats Scissors, you lost :(")
    
else:
    print("Scissors beats Paper, you won! :)")
    
print("Thanks for playing")




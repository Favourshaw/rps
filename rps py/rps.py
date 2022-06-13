from math import comb
from random import choice

#create a list of play options
game_list = ["R", "P", "S"]



while True:
    computer = choice(game_list)

    player = input("Please pck an option." "\n" "R for Rock, P for Paper, S for Scissors?")

    if player == computer:
        print("Tie!.", "player", "(", player, ")", "CPU", "(", computer, ")")
    elif player == "R":
        if computer== "P":
            print("You lose!", "CPU", "(", computer, ")", "covers", "player", "(", player, ")")
        else:
            print("You win!", "player", "(", player, ")", "smashes", "CPU", "(", computer, ")")
        break
    elif player == "P":
        if computer == "S":
            print("You lose!", "CPU", "(", computer, ")", "cut", "player", "(", player, ")")
        else:
            print("You win!", "player", "(", player, ")", "covers", "CPU", "(", computer, ")")
        break
    elif player == "S":
        if computer == "R":
            print("You lose...", "CPU", "(", computer, ")", "smashes", "player", "(", player, ")")
        else:
            print("You win!", "player", "(", player, ")", "cut", "CPU", "(", computer, ")")
        break
    else:
        print("That's not a valid play. Please try again!")
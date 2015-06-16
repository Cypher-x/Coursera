__author__ = 'Win'

# Rock-paper-scissors-lizard-Spock

def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
    else:
        print("Error")


def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
    else:
        print("Error")

import random
def rpsls(player_choice):
    player_number = name_to_number(player_choice)
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)

    print(" ")
    print("Player Chooses:", player_choice)
    print("Computer Chooses:", comp_choice)

    winner = (player_number - comp_number)%5

    if winner == 0:
        print("----Result: Tie Game.")
    if winner == 1:
        print("----Result: You Win.")
    if winner == 2:
        print("----Result: You Win.")
    if winner == 3:
        print("----Result: Computer Wins.")
    if winner == 4:
        print("----Result: Computer Wins.")





    # print a blank line to separate consecutive games

    # print out the message for the player's choice

    # convert the player's choice to player_number using the function name_to_number()

    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()

    # print out the message for computer's choice

    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message

rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

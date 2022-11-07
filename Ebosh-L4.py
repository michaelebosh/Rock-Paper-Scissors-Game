'''

NAME:   Michael Ebosh

DATE:   9/16/2022

ASSN:   LAB ASSIGNMENT L3

DESC:   THE FOLLOWING PYTHON MODULE IMPLEMENTS THE FAMOUS ROCK,
        PAPER, SCISSORS GAME.  THE RULES OF THE GAME ARE SIMPLE.
        EACH PLAYER CHOOSES A ROCK (0), PAPER(1), OR SCISSORS (2).
        THE FOLLOWING ARE WINNING PLAYS:
        
        ROCK BEATS SCISSORS
        PAPER BEATS ROCK
        SCISSORS BEATS PAPER

'''

# COMPUTER CHOOSES ROCK, PAPER, OR SCISSORS BASED ON A RANDOM
# INTEGER CHOICE USING THE RANDINT() FUNCTION.
# COMPUTER IS PLAYER 1
from random import randint
computer_choice = randint(0,2)


# GET THE USER CHOICE, user_choice, USING THE input() function
# TYPECAST AS AN INTEGER
# USER IS PLAYER 2
user_plays = int(input("Please choose (3 - Single Play, 4 - MultiplePlays, 5 - End Game): "))
# IMPLEMENT THE RULES OF THE GAME USING IF-ELIF-ELSE STATEMENTS
# BE SURE TO USE COMPARISON AND BOOLEAN OPERATORS
# IF PLAYER 1 CHOOSES ROCK AND PLAYER 2 CHOOSES SCISSORS, OR
# IF PLAYER 1 CHOOSES PAPER AND PLAYER 2 CHOOSES ROCK, OR
# IF PLAYER 1 CHOOSES SCISSORS AND PLAYER 2 CHOOSES PAPER, THEN
# PLAYER 1 WINS
#
# ELSE IF PLAYER 1 AND PLAYER 2 CHOOSES THE SAME OBJECT, THEN
# IT'S A TIE
#
# OTHERWISE, PLAYER 2 WINS
if user_plays not in range(3,5):
    print("Not a valid option")
    user_plays = int(input("Please choose (3 - Single Play, 4 - MultiplePlays, 5 - End Game): "))
while user_plays == 3:
    user_choice = int(input("Please choose (0 - rock, 1 - paper, 2 - scissors): "))
    if user_choice == 2:
        if computer_choice == 0:
            print("Player 1 wins, rock beats scissors")
        else:
            print("Player 2 wins, scissors beats paper")
    elif user_choice == 0:
        if computer_choice == 1:
            print("Player 1 wins, paper beats rock")
        else:
            print("Player 2 wins, rock beats scissors")
    elif user_choice == 1:
        if computer_choice == 2:
            print("Player 1 wins, scissors beats paper")
        else:
            print("Player 2 wins, paper beats rock")
    elif user_choice == computer_choice:
        print("It's a tie")
    else:
        print("Player 2 wins")
    break
while user_plays == 4:
    user_choice = int(input("Please choose (0 - rock, 1 - paper, 2 - scissors): "))
    if user_choice == 2:
        if computer_choice == 0:
            print("Player 1 wins, rock beats scissors")
        else:
            print("Player 2 wins, scissors beats paper")
    elif user_choice == 0:
        if computer_choice == 1:
            print("Player 1 wins, paper beats rock")
        else:
            print("Player 2 wins, rock beats scissors")
    elif user_choice == 1:
        if computer_choice == 2:
            print("Player 1 wins, scissors beats paper")
        else:
            print("Player 2 wins, paper beats rock")
    elif user_choice == computer_choice:
        print("It's a tie")
    else:
        print("Player 2 wins")
    user_choice = int(input("Please choose (0 - rock, 1 - paper, 2 - scissors): "))
    if user_choice == 2:
        if computer_choice == 0:
            print("Player 1 wins, rock beats scissors")
        else:
            print("Player 2 wins, scissors beats paper")
    elif user_choice == 0:
        if computer_choice == 1:
            print("Player 1 wins, paper beats rock")
        else:
            print("Player 2 wins, rock beats scissors")
    elif user_choice == 1:
        if computer_choice == 2:
            print("Player 1 wins, scissors beats paper")
        else:
            print("Player 2 wins, paper beats rock")
    elif user_choice == computer_choice:
        print("It's a tie")
    else:
        print("Player 2 wins")
    break
while user_plays == 5:
    print("Thank you for playing!")
    break

        
     


    


# PRINT THE WINNER AND THEIR CHOICE



###############
### THE END ###
###############



import random
import sys


def main():
    player = input("Enter your choice in number ( 1 rock/  2 paper /  0 scissors) :")


    if(player==0):
        player = "scissors"
    elif(player==1):
        player = "rock"
    elif(player==2):
        player = "paper"
    else:
        print"Invalid Input Quitting..."
      

    computer = random.randint(0,2)
    if (computer == 0):
        computer = "scissors"
    elif (computer==1):
        computer="rock"
    elif (computer==2):
        computer="paper"


    if (player==computer):
        print("Player is ",  player, "Computer is ",computer," tie")

    elif (player == "rock"):
        if (computer == "paper"):
            print("Player is ",player, "Computer is ",computer," You Lost!")
        else:
            print("Player is ",player, "Computer is ",computer," You Win!")


    elif player == "paper":
        if (computer == "rock"):
            print("Player is ",player, "Computer is ",computer," You Win!")
        else:
            print("Player is ",player, "Computer is ",computer," You Lost!")


    elif (player == "scissors"):
        if (computer == "rock"):
            print("Player is ",player, "Computer is ",computer," You Lost!")
        else:
            print("Player is ",player, "Computer is ",computer," You Win!")
main()

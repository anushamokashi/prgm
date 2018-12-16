import random
import sys
def func():
	user_choice=get_user_choice()
	computer_choice=get_computer_choice()
	dec(user_choice,computer_choice)

def get_user_choice():
    u=input("enter  your choice 0/1/2\n")
    if(u == 0):
	u="rock"
	print "user choose",u
    elif(u==1):
	u="paper"
	print "user choose",u
    elif(u==2):
	u="scissors"
	print "user choose",u
    else:
	u="invalid choice"
	print u
    return u


def get_computer_choice():
    com=random.randint(0,2)
    if(com == 0):
	com="rock"
	print("computer chooses rock")
    elif(com==1):
	 com ="paper"
	 print("computer choose paper")
    else:
	 com="scissors"
	 print("computer choose scissors")
    return com


def dec(user_choice,computer_choice):
    if(computer_choice==user_choice):
           print("tie")

    elif(computer_choice=="rock" and user_choice =="paper"):
	   print"paper win"
    elif(computer_choice=="rock" and user_choice=="scissors"):
	   print("rock win")
    elif(computer_choice=="paper" and user_choice =="rock"):
	   print("paper win")
    elif(computer_choice == "paper" and user_choice =="scissors"):
	   print("scissor win")
    elif(computer_choice == "scissor" and user_choice =="rock"):
	   print("rock win")
    elif(computer_choice =="scissor" and user_choice =="paper"):
	   print("scissor win")
    else:
	  print"none"


func()



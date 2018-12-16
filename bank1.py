balance=1000.0

print"""
please choose the option
	1.name
	2.withdraw
	3.Deposit
	4.balance
	5.quit
"""

option=int(input("enter option"))

if option==1:
    name=raw_input("enter the name")
    print name

if option==2:
    print("balance",balance)
    withdraw=float(input("enter the withdraw amount"))
    if(withdraw>0):
        balance1=balance-withdraw
    	print balance1
    elif(withdraw>balance):
	print"no amount in account"
    else:
	print"no withdraw made"


if option==3:
    print("balance",balance)
    deposit=float(input("enter the deposit amount"))
    if(deposit>0):
	balance1=balance+deposit
        print(balance1)
    else:
	print"no deposit"

if option==4:
    print"balance",balance

if option==5:
    exit()


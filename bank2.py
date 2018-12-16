class BankAccount:

    def __init__(self,name):
	self.name=name
	self.balance=0


    def deposit(self,amount):
	print "the deposit amount"
	self.amount=amount
	self.balance+=amount
	print self.balance
	
class MinimumBalanceAccount(BankAccount):
   
    def withdraw(self, amount):
         if self.balance - amount < 500:
             print 'Sorry, minimum balance must be maintained.'
         else:
             
	     print "the withdraw amount"
	     self.amount=amount
	     self.balance-=amount
	     print self.balance
 
	
print""" 
	1.Name
 	2.deposit
	3.withdraw
	4.exit"""

			
while(1):

	n=input("enter the choice 1/2/3\n")
	

	if n==1:
  	     name1=raw_input("enter the name")
  	     name=BankAccount(name1)
	     name3=MinimumBalanceAccount(name1)
  	     

	

	if n==2:
             
		
    	     deposit1=input("enter the deposit amount")
    	     name3.deposit(deposit1)
	     


	if n==3:
   	     withdraw1=input("enter the withdraw amount")
    	     name3.withdraw(withdraw1)
	     
	if n==4:
	     exit()
	


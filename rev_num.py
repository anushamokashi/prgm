'''x=input("enter the num")
reverse=0
while (x):
	reverse = reverse * 10
	reverse = reverse + x% 10
	x=x/10
print(reverse)'''


num=input("enter the num")
print (num[::-1])
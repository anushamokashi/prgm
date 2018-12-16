num=input("emter the num")
n1=0
n2=1
print "%s \n "%n1
print "%s"%n2
for num in range(1,num):
   for i in range(2,num):
       if (num%i==0):
       	    break
       else:
       		print(num )
       		print("\n")
       		break

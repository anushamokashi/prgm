char = raw_input("Enter the character to draw: ")
size = int(raw_input("Enter the size: "))

s=""
p=0
for i in range(1, size):
        print char*i
    	p = p+int(char)
        s=s+str(p)
print s[::-1]


    


'''def digit_sum(n):
    num_str = str(n)
    sum = 0
    for i in range(0, len(num_str)):
        sum += int(num_str[i])
    return sum
 
sum()'''

'''code=2
an=2 
al=4
mo=6
print"%s" %code
print "%s %s" %(code,code)
print "%s %s %s" %(code,code,code)
print "%s %s %s" %(mo,al,an)'''
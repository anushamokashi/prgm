i = 0
numbers = []

while i < 6:
	print "at the top i is %d" %i

	numbers.append(i)

	i= i + 1
	print "the numbers now", numbers
	print "at the bottom i is %d" %i

print "the numbers:"

for number in numbers:
	print number	
	

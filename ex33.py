i = 0
numbers = []

def print_numbers():
	for i in range(0, 6):
		print "At the top i is %d" % i
		print "Adding %d to the list." % i
		i += 1
		numbers.append(i)
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
		
print_numbers()

print "The numbers: "
		
for num in numbers:
	print num	

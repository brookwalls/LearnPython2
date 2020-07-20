def add(a, b):
	print "ADDING %d + %d" % (a, b)
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b
	
def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b
	

print "Let's do some math with just functions!"

age = add(30.0, 5.0)
height = subtract(78.0, 4.0)
weight = multiply(90.0, 2.0)
iq = divide(100.0, 2.0)

print "Age: %d, Height: %d, Weight: %d, IO: %d" % (age, height,weight,iq)


# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "\nCan you do it by hand?\n"

print "Here another puzzle."

next = multiply(weight, add(age, divide(iq, subtract(height, 79.0))))

print "The answer is: ", next, "\nCan you do that one by hand?"
 


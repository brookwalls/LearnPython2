# x is equal to "There are 10 types of people."
x = "There are %d types of people." % 10
# binary equal the string binary
binary = "binary"
# do_not equal don't
do_not = "don't"
# y equals "Those who know binary and those who don't."
y = "Those who know %s and those who %s." % (binary, do_not)

# prints x
print x
# prints y
print y

# prints "I said: x"
print "I said: %r." % x
# prints "I also said: y"
print "I also said: '%s'." % y

# hilarious equals False
hilarious = False
# joke_evalution equals "Isn't that joke so funny?!
joke_evaluation = "Isn't that joke so funny?! %r"

# prints joke_evaluation and then hilarious
print joke_evaluation % hilarious

# w equals "This is the left side of..."
w = "This is the left side of..."
# e equals "a string with a right side."
e = "a string with a right side."

# prints and w ans e together
print w + e 



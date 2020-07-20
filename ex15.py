# when you run the file you have to include argv
#from sys import argv 

# the input argu will be set to filename
print "What's the name of the file you want to open?"
#script, filename = argv
filename = raw_input("- ")
# opens the file
txt = open(filename)

# print "Here's your file filename:
print "Here's your file %r:" % filename
# print out the file
print txt.read()

# print "Type the filename again:"
print "Whats the filename again:"
# saves the filename to file_again

#script, file_again = argv
file_again = raw_input("> ")

# opens the file and saves it to txt_again
txt_again = open(file_again)

# print out the file
print txt_again.read()
 
txt.close()
txt_again.close()


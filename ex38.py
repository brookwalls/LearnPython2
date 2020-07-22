# ten_things is equal to "Apples Oranges Crows Telephone Light Sugar"
ten_things = "Apples Oranges Crows Telephone Light Sugar"

# prints out "Wait there's not 10 things in that list, let's fix that."
print "Wait there's not 10 things in that list, let's fix that."

# ten_things.split(' ') to python is split(ten_things, ' ')
# stuff is set to split(ten_things, ' ')
stuff = ten_things.split(' ')
# more_stuff is set to ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# it will go through the code while len(stuff) is not 10
while len(stuff) != 10:
	# more_stuff.pop() to python is pop(more_stuff, )	
	# next_one is set to pop(more_stuff, )
	next_one = more_stuff.pop()
	# prints Adding: next_one
	print "Adding: ", next_one
	# stuff.append(next_one) to python is append(stuff, next_one)
	stuff.append(next_one)
	# prints There's len(stuff) items now.
	print "There's %d items now." % len(stuff)

# prints There we go: stuff	
print "There we go: ", stuff

# prints "Let's do some things with stuff."
print "Let's do some things with stuff."

# prints stuff[1]
print stuff[1]
# prints stuff[-1]
print stuff[-1] # whoa! fancy
# stuff.pop() to python is pop(stuff, )
# prints pop(stuff, )
print stuff.pop()
# ' '.join(stuff) to python is join(' ', stuff)
# prints join(' ', stuff)
print ' '.join(stuff) # what? cool!
# '#'.join(stuff[3:5]) to python is join('#', stuff[3:5])
# prints join('#', stuff[3:5])
print '#'.join(stuff[3:5]) # super stellar!

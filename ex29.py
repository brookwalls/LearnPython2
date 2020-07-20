people = 20
cats = 30
dogs = 15


if people < cats:
	print "Too many cats! The world is doomed!"
	
if people > cats:
	print "Not too many cats! The world is saved!"
	
if people < dogs:
	print "The world is drooled on!"
	
if people > dogs:
	print "The world is dry!"
	
print "There are %d dogs and %d people." % (dogs, people)
dogs += 5
print "There are %d dogs and %d people." % (dogs, people)

if people >= dogs:
	print "People are greater than or equal to dogs."
	
if people <= dogs:
	print "People are less than or equal to dogs."
	
if people == dogs:
	 print "People are dogs."
	 
	 

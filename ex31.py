print "You enter a dark room with three doors.\nDo you go through door #1 or door #2 or door #3?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the cake."
	print "2. Scream at the bear."
	print "3. Try to walk away."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good job!"
	elif bear == "2":
		print "The bear eats your legs off. Good job!"
	elif bear == "3":
		print "\nWhat's your plan?"
		print "1. Walk away backwards."
		print "2. Turn around and walk away."
		print "3. Walk side ways."
			
		walk = raw_input("> ")
			
		if walk == "1" or walk == "2" or walk == "3":
			print "You strip and get impelled by roots and die. Good job!"
		else:
			print "A rock fell on you and you were crashed to death slowly. Good Job!"
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
	print "You star into the endless abyss at Cthulhu's retina. What do you do?"
	print "1. Eat blueberries."
	print "2. Eat yellow jacket clothespins."
	print "3. Understand revolovers yelling melodies."
	print "4. Try to find a way out."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	elif insanity == "3": 
		print "The insanity rots your eyes into a pool of muck. Good job!"
	elif insanity == "4":
		print "You turn around and star into the endless abyss\nat Cthulhu's retina. You die of sadness! Good job!"	
	
	else:
		print "You stumble around and fall on a knife and die.\nGood job!"
elif door == "3":
	print "You open the door and see the sun and tree.\nYou run outside and fall straight off the cliff. Good job!" 
else:
	print "You die of dehydration and starvation, never making a choose. Good job!"
		

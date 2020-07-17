name = 'Brook A Walls'
age = 19 # not a lie
height = 5.15 * 12 # inches
height_in_cm = height * 2.54
weight = 125 # lbs
weight_in_kilo = weight / 2.20462
eyes = 'Blue/Green'
teeth = 'white'
hair = 'Blond'

print "Let's talk about %s." % name
print "She's %d inches tall." % height
print "She's %d centimeter tall." % height_in_cm
print "She's %d pounds." % weight
print "She's %d kilo." % weight_in_kilo
print "That's a prefect weight."
print "She's got %s eyes and %s hair." % (eyes, hair)
print "Her teeth are %s." % teeth
print round(1.73334243)

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

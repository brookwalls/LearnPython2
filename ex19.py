def cheese_and_crackers(cheese_count, boxes_of_crackers):
	print "You have %d cheeses!" % cheese_count
	print "You have %d boxes of crackers!" % boxes_of_crackers
	print "Man that's enough for a party!"
	print "Get a blanket.\n"
	

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)


print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

def pizza_time(pizza_boxes, diff_type_of_pizza):
	print "We have %d pizza boxes!!!!" % pizza_boxes
	print "We have %d different types of pizza!" % diff_type_of_pizza
	print "Party time!"
	print "Puts some music on!\n"
	
pizza_time(100, 37)


pizza_boxes = 25
diff_type_of_pizza = 7

pizza_time(pizza_boxes, diff_type_of_pizza)


pizza_time(100 + 20, 5 + 6)


pizza_time(pizza_boxes + 1000, diff_type_of_pizza + 10)

print "How many boxes of pizza do you have?"
pizza_boxes = int(raw_input())
print "How many different types of pizza do we have?"
diff_type_of_pizza = int(raw_input())

pizza_time(pizza_boxes, diff_type_of_pizza)

	



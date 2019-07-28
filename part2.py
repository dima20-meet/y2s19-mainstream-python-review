# Part 2 of the Python Review lab.

def encode(x, y):
	if  1 < y < 250 and 500 < x < 1,000:
		return x*y

	else:
		print "Invalid input: Outside range"
		return None

def decode(coded_message):
	pass
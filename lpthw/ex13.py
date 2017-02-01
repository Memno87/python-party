from sys import argv

age = raw_input("How old are you? ")

script, first, second, third = argv



print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
print "So, you're a %r, %r %r and there ain't no lie." % (
	first, second, third)


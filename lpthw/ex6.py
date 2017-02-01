# There are 10 types of people
x = "There are %d types of people." % 12
binary = "binary"
do_not = "don't"
# Those who know binary and those who don't
y = "Those who know %s and those who %s" % (binary, do_not)

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

w = "This is the left side of..."
e = "a string with a right side."

print x
print y
print w + e 

print "I said: %r" % x
print "I also said: '%s'." % y

print joke_evaluation % hilarious


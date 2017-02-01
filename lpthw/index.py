'a script' #a script is a series of code which, when run, will perform an action
'a variable' #a variable is just a way of naming something (a function / action / text) instead of having to repeatedly type it out

python title.py #this will run a python script as long as the command line is in the correct folder
python title.py sample.txt  #if a script contains two variables in an arg, this will be entered after the Python file name
print #this will print the accompanying string in the command line if the script is run
"text" #an example of a string - between "" we can put any characters
+ - / * #as you expect!
%
<
>
<=
>=
"test" %
"test" % (var1, var2)
test = "test" #an example of setting a 
"%d"
"\n" #when displayed in the command line, this will cause a break and a new line to be shown
"%r"
"%s"
\t* 

"""
Line 1
Line 2
Line3
 """

test = raw_input()
raw_input("?")

prompt = '>'
test = raw_input(prompt)

print "So, you're %r, %r and %r" % (var1, var2, var3)
y = raw_input("Name? ")
from sys import argv
var1, var2, var3 = argv 

target = open(filename) #this defines the variable 'target' and dictates that target shoudl open the file referenced (filename - which is referenced in the opening argv)
print target.read() #this will print the file referenced before the . (as long as the variable is defined previously)
target = open(filename, 'w') 
target.truncate() #this will erase all data in the files referenced in the variable 'target'
target.write #this will write to the file referenced in the variable 'target'

def print_all(f): 
	print f.read()

def rewind(f): 
	f.seek(0) #this will examine the file and move the the byte detailed in the number.

def print_a_line(line_count, f): 
	print line_count, f.readline()
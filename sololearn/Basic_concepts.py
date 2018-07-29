# This is a simple 'print' command. The result would be 'hello world'
print ("hello world")

# Python is able to complete simple maths equations such as +, -, /, the use of () to order
print (5 + 2)
print (12 + (5 - 3))

# When completing a division on two integers (whole numbers), the result will alwaus be a 'Float' (a number with a decimal place)
print (10 / 5)

# Exponentiation can be completed by using the **. The example below = 20,736
print (12 ** 4)

# Quotients can be calculated by using 'floor division' //. This will calculate the the amount of times the numbers can be divided into each other. The example below = 2
print (12 // 5)

# Remainders can be calculated using the 'modulo' %. This will divide the two numbers and calculate the remainder. The example below = 3
print (8 % 5)

# Strings are for when you need to use text in Python. Generally, you should use '' rather than "". Within a tring, there are number of characters that you can't use called 'escape characters'. An example of this would be a ' which would normally end the string. To avoid this closing the string, you must add a \ before the 'escape character'. If you would like the text to be displayed a new line, you can use '\n'
print ("This is an example string.\nIt\'s very important that you use \ when using characters which would end the string")

# Python has a quicker way of creating new lines (avoiding having to use the \n). You can do this by using """. Example below
print ("""My anaconda don\'t.
My anaconda don\'t""")

# You can use 'raw_input' (or just input in Python3) to prompt a user for input. The below code will display this back to them. 
a = input ("Do you like booty? ")
print ("Of course the answer is "+a)

# Concatenation: within Python you are able to combine two (or more) strings using the following method: To note: this is used for adding strings together. If you try and use this for adding a combindation of strings and integers, the code will error
print("Big"+"booty")

# Using the above method, you can also multiply (to note, other forms of calcultion or floats don't work) strings by integers, see below:
print("booty"*8)

# Python allows you to convert 'type'. You could convert a string to an integer to allow calculation to be completed. You can also do this for converting to strings and floats
print(int("2")+int("17"))
print(float(2)+12)
print(str(2+4))

# Here are some examples of taking some raw input from a user (which will be stored as a string) and convering to a float / integer. This will allow you to user inputs from a user to create calculations.
x = float(input ("Enter a number: "))
y = float(input ("Enter another number: "))
print (x + y)

b = int(input ("Enter a number: "))
c = int(input ("Enter another number: "))
print (b + c)

# Creating variables will be key to future programming. We have used them previously to store user inputs, futher examples will be seen below. You can change variables as often as you like within the code. For instance, we can see above the var a was used for asking whether you like booty, but also to represent 22.
a = 22
print(a)
print(a*55)
e = int(input ("Multiply by how many? "))
print(a*e)

# There are rules around variables. They must consist of letters, numbers and underscores only and can not start with a number. To note, Python is case sensitive so Var1 and var1 are not the same. Some examples below:
this_is_a_variable = "Variable 1"
Variable_2 = "Variable 2"
print(this_is_a_variable)
print(Variable_2)

# You can also delete variables with the 'del' function:
# a=22
# print(a)
# del a
# print(a)

# Python also has the option to use 'in-place operators'. These can be used to modify a variable whilst keeping the code concise. The examples below show how you can take a variable, then multiply it by 3. You can also do this -, +, %, /
a = 22
print(a)
a*=3
print(a)
a%=4
print(a)

# In-place operators can also be used on strings / floats.
a = "eggs"
print(a)
a*=10
print(a)



"""operators:
+ addition
- subtraction
/ division
* multiplication
** power
% devide and return the remainder (useful for games e.g. rnum % 52 generates a random card)


() > ** > */ > + > left to write


""" 
x = 1 + 2*3 - 4 / 5 ** 6 # ~7
print (x)

"""
Types: all things in python have a type, including string, interger and float
operators are dependant on type ex: + adds integers and floats, but concatonates strings
errors out if trying to merge multiple types with an operator

type(variable) tells you the type
float(variable) converts int to float
integer division always produces a float value, even if both divisors are ints
can also use int() and float() to convert between strings and integers, only works for digits

can use the input command
input("queue"), waits for user input, and outputs the user entry as a string
"""
string = "sad"
inte = 1
inte + string #should type error out

print(2/1) #should produce 2.0

"""
First useable program:
converts between USA and europe elevator conventions
"""
inp = input("Floor in Europe? ") # asks for europe floor
usf = int(inp) + 1 # adds one to convert to US
print ("US floor is", usf) # produces result


"""
Additional exercises:
e2, write a program that uses the input command to prompt a user for their name and then welcomes them
e3, write a program to prompt the user for hours and rate per hour to compute gross pay
"""

e2nam = input("what is your name? ")
print("Hello", e2nam)

e3hour = float(input("how long did you work? "))
e3Rate = float(input("what is your hourly wage? "))
print("you should earn:", e3hour * e3Rate)
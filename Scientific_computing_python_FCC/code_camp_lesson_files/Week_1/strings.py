"""
Strings are sequences of characters, + is cat, numbers can be strings (fully number strings can be converted to ints and floats)

reading and converting: 
most common initial datatype
input() always gives a string

looking inside with square brackets (index operator):
[]
strings labeled 0-x
banana
012345

you will error out if you index beyond a string

len() gives length-1 of a string


Looping through a string
"""
#fruit = "banana"
#index = 0
#while index <len(fruit):
#    letter = fruit[index]
#    print(index,letter)
#    index = index + 1

#prettier loop, always do a for over a while if possible
#for c in fruit:
#    print(c)

#count=0
#for c in fruit:
#    if c == "a":
#        count += 1
#print(count)


"""
Slicing strings: advanced indexing
s = "monty python"
print(s[0:4])
prints mont
index is upto but not including the final number

can eliminate either first or last number to have python assume the first or final thing on a string

+ doesnt add a space!

in can be used like ==, except searching for a char in a string

can also use == and < in strings, but that seems quite weird. good to know i suppose

python has a number of string functions in the string library

example:
.lower() reduces all components of the string to lowercase
.function() is an object oriented function
function() is a non-object oriented function


Useful string functions
dir-> gives a list of all possible functions

find() finds a substring within a string, gives position of the first character, or -1 if not in the string

.upper() provides uppercase 

.replace() functions the same way as ctrl D

.lstrip/rstrip(), remove all spaces at the left or right of string respectively, .strip() does both

"""

#dir(fruit)

"""
Similar to R you can find two positions and extract between them:

example: extracting the university from an email:

data = "email@institution.ca.gov.hackerman 12:12:20"
atpos = data.find("@")
sppos = data.find(" ")

uni = data[atpos+1:sppos]
print(uni)
"""

#exercise: take the following python code:
string = 'X-DSPAM-COnfidence: 0.8475 '

#use find and slicing to extract everything after the colon and convert to a number with float

colon = string.find(":")
string = string[colon+1:]
#string = string.strip() this is redundant, as float ignores spaces!
number = float(string)
print(number)
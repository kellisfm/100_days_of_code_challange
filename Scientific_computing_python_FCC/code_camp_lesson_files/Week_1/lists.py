"""
algorithm: set of rules or steps to solve a problem
data structures: means of organizing data in a computer
Lists are our first data structure method

variables only have 1 assignments at a time, collections like lists allow multi assignments

help= ["h","e","l","p"] 4 item string list
can do lists in lists:
list = [1,[1,2,3],[],2]

lists are mutable, can be changed, strings cannot be changed (Immutable)
can do shit like:
list[2] = "string"
len() works with lists, tells number of items
range() returns a list of numbers that range from 0 to 1 less than the parameter, common motif range(len(list)) to loop an entire list

for statements love lists, work through them in order

looping motifs:
for l in list:
    print(l)
loops through all values, assigning the value to l

for i in range(len(list)):
    l = list[i]
    print(l)
loops through all values, assigning the value number to i, and allowing you to extract the value of i

both work, but if you're just looking to print all values, 1 works better

other list operations:
+ cat also works with lists: merges two lists example:
[1,2,3] + [4,5,6] -> [1,2,3,4,5,6]

can be sliced in the same way as strings, example:
list[:9]
will take the first 9 values of the list (pos 0-8)

list methods: dir() again is incredibly useful!

making lists:
variable = list() generates empty list
variable.append('values') adds a value in the last position

can check if an value is included with in, provides boolean response, doesnt modify list.
lists hold order and can be sorted

variable.sort does a rudimentory sort, effective for well put together lists
other ones are 
max() highest value
min() lowest value
sum() total value

can use this to replace our earlier setup for generating sum, average, and count
"""
#l = [1,2,3,4]
#dir(l)

"""
strings and lists:
can split a string into a list with varibale.split()
eg: var = "i hate everything"
var.split() -> ["i", "hate", "everything"]
this is just more efficient than slicing everything( which is also possible)
split treats multiple spaces as a single space, also treats newlines as a split

can modify: var.split(";") will split at semicolons, less good than blancs as it will not treat multisetups as a single. 

"""
#exercise: get mailbox data, extract the third block from all subject lines
fhandle = open("mbox-short.txt")
list3rdword = list()
for l in fhandle:
    l = l.rstrip()
    l = l.split()
    if len(l) < 3 or l[0] != "From":
        continue
    list3rdword.append(l[2])
print(list3rdword)


"""
Dictionaries: a bit messier than lists, not ordered. However, excellent means of
data storage

they are a bag of values (unordered), but where all values have tags and are easily accessible.

pythons most powerful datastructure, similar to associatve arrays in php.

variable = dict() generates blank dictionary
can add by running
variable[key] = item

Basically the same as a list, except key replaces positional indexing

dictionary literals: {} rather than the [] found in lists
example:
dicitionary{key1:value1, key2:value2,....}

common applications for dictionaries:
histograms! counting the frequency of things
can create a key and increase it by 1 everytime something appears.
is name in dictionary? no, add name, yes add one to value

Histogram builder example:
"""

#counts = {}
#letters = ['a', 'b','c','d','e','a','a','a','b','b','c','d','c','s','q','e','t']
#for s in letters: #runs through all the letters in the list
#    if s not in counts: # checks if the letter is in the dictionary
#        counts[s] = 1 #adds it to dictionary with base count 1 if no
#        continue #skips to next letter
#    counts[s] += 1 #adds 1 to the count if yes
#print(counts)

"""
these if else statements are so common that the get() function does the same thing as an if else statement!

same program as above but with get(keyname,value)
notes: value defaults to none, if get does not find the appropriate keyname it will give the value assigned, else it returns the value of the keyname
"""
##counts = {}
#letters = ['a', 'b','c','d','e','a','a','a','b','b','c','d','c','s','q','e','t']
#for s in letters:
#    counts[s] = counts.get(s,0) + 1 #finds
#print(counts)

"""
looping through dictionaries:
for key in counts:
    print(key, counts[key])
will result in the print of the dictionary with each key and value on a line

can get list of keys with
list(dicvar)

or with 
dicvar.keys()

can get values with
dicvar.values()

or list of tuples with
dicvar.items()

can loop through the dictionaries quite elegantly with
for a,b in dicvar.items():
    print(a,b)
"""
#exercise: count the most common word in a user selected .txt file

#steps: 1 get user input of filename and open it (if it exists)
#2: loop through each line, adding each novel word to a dictionary or increasing its value by one should it exist
#3: have a loop run through our dictionary, evaluating wheather each entry is larger than our previous best and presenting that value and key at the end

#get user input and open file
ufile = input("Which file would you like to know the most common word in? ")
try:
    oufile = open(ufile)
except:
    print("Please try again, with a real file this time! ")
    quit()

#create a dictionary, and convert the file from individual lines into a list of strings (stripping out newlines)
counts = {}
for l in oufile:
    l = l.rstrip()
    l = l.split()
    for s in l: #Add each new word to the dictionary, and increase any extant words value by 1
        counts[s] = counts.get(s,0)+1

#cycle through the dictionary, replacing any each successive lower count with a higher one
bigkey = None
bigcount = None 
for key,count in counts.items():
    if bigcount is None or count > bigcount:
        bigkey = key
        bigcount = count 
print(bigkey)
print(bigcount)


#lets generate a top ten words list now:
#two methods: list comprehension, and classic algorithms
ordered = sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) #list comprehension method: generates a list of v,k tuples which were created from the values k,v out of the 
#counts.items() function
print(ordered[:10])

#algorithm method needs to:
#1 convert the counts dictionary into a list of reversed tuples [(b,a),...]
#2 sort the list in descending order
#3 print the top ten words

#part 1: converting to a list
countlist = []
for k,v in counts.items() :
    countlist.append( (v,k) ) #append only takes 1 item at a time, need to append as a tuple (brackets in brackets)

countlistsorted = sorted(countlist, reverse=True) #reverse sort for descending order

print(countlistsorted[:10])

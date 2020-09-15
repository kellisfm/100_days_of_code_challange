# e1 write two functions: the first is called chop(list) which replaces the first and last elements with None
#the second is called middle which takes a list and returns it without the first or last elements
import re
def chop(list1): #replaces the first and last elements with None values
    for i in [-1,0]: #loops through the selected elements (in this case first, 0, and last, -1)
        list1[i] = None
    return list1
help = [1,2,3,4,5,6,7]
oh = ["1","1"]
print(chop(help))
print(chop(oh))
def middle(list2): #deletes the first and last elements
    for i in [-1,0]:
        del list2[i]
    return list2
print(middle(help))
print(middle(oh))

#e2 open the mail file and read it line by line, for each line split it into its constituant words and check if they are already in a list, if no: add it. Print the list in alphabetical order
wordlist = []
mbox = open("mbox-short.txt")
for line in mbox: #splitting each line after stripping the rightside whitespace
    line = line.rstrip()
    llist = line.split()
    for word in llist: #getting the individual words
        if bool(re.search("[^a-z]",word.lower()))==False and word.lower() not in wordlist: #only grabbing words, not email adressess etc
            wordlist.append(word.lower())
wordlist.sort() #sort
print(wordlist) #print


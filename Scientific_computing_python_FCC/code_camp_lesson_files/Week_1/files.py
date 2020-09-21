"""
reading files:
bringing the secondary memory into the equation!

we will later be getting to databases etc.

Text files are just sequences of lines of text separated by newline characters \n (this is recognized as one character not two in python)
note: print() always adds a \n to the end of a print statement

using open():
handle += open(filename,mode) gives us a variable called handle which we can use to manipulate the file in question
filenem must be a string
mode is optional: use r for reading, w for writing

when file is missing? Traceback error!

often for loops are used for reading files:
handles just treated as a sequence of lines
example:
xfile = open('file.txt')
for l in xfile:
    print(l)

this loop will print each line in a file

count = 0
for l in xfile:
    count += 1
print("numlines:",count)
this loop will count the number of lines in a file

can also read the file as a string: but careful, generates a very large string if file is large

xfile = open("file.txt")
inp = xfile.read()
print(len(inp)) #this tells you how large the string is
print(inp[:200]) #prints first two hundred char

searching for a file:
fhand = open("file")
for line in fhand:
    if line.startswith("From:"):
        print(line)
this setup actually double spaces, as print always adds an extra \n

strip removes spaces and newlines!

fhand = open("file")
for line in fhand:
    line = line.strip()
    if line.startswith("From:"):
        print(line)
fixed!

fhand = open("file")
for line in fhand:
    line = line.strip()
    if not line.startswith("From:"):
        continue
    print(line)
does the same thing, but skips any lines that dont start with from:

Complete mailbox subject line counter:

#fname = input('Enter the file name! ')
try:
    fhand = open(fname)
except:
    print("error, file doesn't exist")
    quit() #useful for terminating the python program without traceback (more professional)
count = 0
for line in fhand:
    if line.startswith('Subject: ') :
        count += 1
print("There were", count, "subject lines in", fname)

"""
# exercise: write a program to read through a file and print the contents in all uppercase:

fname = input('Enter the file name of interest! ')

try:
    fhand = open(fname)
except:
    print("this file doesn't exist, please try again.")
    quit()
for line in fhand:
    line = line.strip()
    line = line.upper()
    print(line)

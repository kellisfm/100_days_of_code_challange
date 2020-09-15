"""
regex exercises:
1) write a grep function (a function where a user enters a regex and the function checks how many lines in the document match it)
"""
import re
def grep(regex,filename): #for whatever reason this doesnt work multiple times if we let the user run the open, and then put the handle through the function. Worth looking into why
    handle = open(filename)
    count = 0
    for line in handle:
        if re.search(regex,line):
            count += 1
    print(count)
reg = "From "

grep(reg,"mbox-short.txt")
grep(r"\d\d:\d\d","mbox-short.txt")
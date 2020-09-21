"""
Tuple exercises (chapter 10 py4e):
revise or remake a program to open the mbox file and perform the following tasks:
print the person with the most emails sent to us,
count the number of emails recieved at each hour of the day, print them out 1/line
count the occurance of each letter, print only lowercase a-z

By Kai Ellis
2020-09-12
"""
#Steps:
#1) open the file, start 3 dictionaries (one for each task)
#2) loop through the mailbox-short, checking for lines that start with from (these are the only ones that matter for E1/2) or lines that have a letter (A-z req for E3)
#3) to solve 1/2 will need to regex out the hour and the full email from the From: line, for 3 im not sure yet, maybe regex for position of all non-alpha char and delete them?.
#4) add all matching things to dictionaries, with the classic looping dic[key] = dic.get() setup for creating histograms
#5) if neccissary sort with list comprehension
#6) print
import re
timedic = {}
addic = {}
letterdic = {}
hand = open("mbox-short.txt")
for line in hand: #loop through each line
    line = line.rstrip()
    if re.match(r"From\s",line): #find lines that start with From
        etime = (re.findall(r"From\s(.*@.*?)\s.*\s(\d\d):",line)) #extract the email and time, and add both to seperate dictionaries
        addic[etime[0][0]] = addic.get(etime[0][0],0) + 1 
        timedic[etime[0][1]] = timedic.get(etime[0][1],0) + 1
    if re.search(r"[A-Za-z]",line): #find lines that have at least one letter
        word = line.split() #split into words
        word = line.lower() #force lowercase
        for letter in word: #cycle through the word letter by letter
            if re.match(r"[a-z]",letter): #check if we have a letter or something else, add to dic if letter
                letterdic[letter] = letterdic.get(letter,0)+1
freqad = ("temp",-1)
for k,v in addic.items(): #cycle through the address list and check if the current sender has sent more than our previous highscore, replacing if yes
    if v > freqad[1]:
        freqad = (k,v)
print("most frequent corrispondant")
print(freqad)
timesort = sorted( [ (k,v) for k,v in timedic.items() ] )
print("Emails by time:")
for i in timesort:
    print(i,"\n")
print("most frequent letters:")
print( sorted( [ (v,k) for k,v in letterdic.items()], reverse=True )) #list comprehension for sorting by most frequent letter






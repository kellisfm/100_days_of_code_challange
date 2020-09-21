#write a program to read through the mail-log file, build a histogram using a dict to count how many messages came from each email caccount and print
#also print the person with the highest number of emails

#steps:
#1) open the mail file, create an empty dictionary, and set up a loop to read each line in the mail file
#2) for each line that contains a subject (From: ) extract the email address
#3) if the address matches one in the dictionary, add one to that fellow's email count, else, add it too the dictionary
#4) sort the email adressess by value (in this case number of emails) and print the first entry, along with the full unsorted dictionary
import re


mail = open("mbox-short.txt") 
emailtime = {}

for line in mail:
    line = line.rstrip()
    if re.match("From ", line): #dont bother with == statements when using re, they break. If they are needed, convert to bool first
        line = line.split()
        for word in line:
            if re.match(r".*@.*",word):
                emailtime[word] = emailtime.get(word,0) + 1
                

print("Most frequent corrispondance is with:", sorted ( [ (v,k) for k,v in emailtime.items() ],reverse = True )[0] )
print("Full list of contacts:", emailtime)


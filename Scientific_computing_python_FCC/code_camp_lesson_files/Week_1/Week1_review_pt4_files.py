#exercise:
#write a program to read through a user generated file, read through and look for lines that start with X-DSPAM-Confidence and extract the floating point vlaue, printing the average spam confidence
#also produce the top 10 words and include an easter egg that gives a silly response if the user enters Queen's for the filename

#steps:
# 1 input for file, open selected file (safe error if not valid), include an if statement for the easter egg
# 2 check specifically for lines starting with X-DSPAM-Confidence, regexing out the neccissary values
# 3 include variables count and total of the confidence values so we can calculate average
import re
fname = input("Please enter the full name of your file of interest: ")
try:
    fhand = open(fname)
    print(fname, "successfully opened")
except:
    if fname == "Queen's":
        print("Rickards")
    else:
        print("that file was not found in the current working directory, please check your typing or the location of your file")
    quit()
count = 0
total = 0
for line in fhand:
    if re.match("X-DSPAM-Confidence:",line):
        confidence = re.findall(r"\s(0\.[1234567890]*)\s",line)
        count += 1
        total += float(confidence[0])
        
average = total/count 
print("Number of potential spam emails: %g" %count,"Average spam confidence %g" %average, sep ="\n")


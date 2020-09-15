"""
since HTTP is nearly universal, URLLIB has been created to do all the socket work and to format webpages like a proper txt file.
Damn, thats noice
"""
import urllib.request, urllib.parse,urllib.error

counts = {}
fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt") #request this webpage
for line in fhand:
    words = line.decode().split() #still need to have a decode line as it arrives in the form of bytes
    for word in words:
        counts[word] = counts.get(word,0) +1
print(counts)


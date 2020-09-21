
import re
from linkscraper import linkgrab # apparently you have to add the from... if you want things to work , the more you know
from time import perf_counter

def main():
    tally = {} #open an empty dictionary which will serve as our reference list
    queue = ["https://nuclear-throne.fandom.com/wiki/Characters"] #open a list of pages we have not yet visited
    ts = perf_counter()
    while len(queue) > 0:
        url = queue.pop(0) #take the first one from our list of pages and save it
        url_intro = re.findall(r".*/wiki/", url)
        print(url)
        links = linkgrab(url) #the time intesive process: takes ~100,000 x longer than the tallying section
        for link in links:
            if link == url: #makes sure articles can't self reference
                continue
            elif link in tally.keys(): #adds one to the tally if the article in question has already been referenced
                tally[link] += 1
            else: #appends the tally with a new entry and a default count of 1 if it's not already there 
                queue.append(url_intro[0] + link)
                tally[link] = 1
    orglist = sorted( [ ( v,k ) for k,v in tally.items() ], reverse = True )
    tf = perf_counter()
    print("Time elapsed:", tf-ts)
    with open(r"wiki_importance_output.txt","w") as handle:
        handle.writelines("%s: %s\n" %(k, v) for v,k in orglist)
    



main()

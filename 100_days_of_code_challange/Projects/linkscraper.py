"""
The goal of this function is to go into a web page and grab all the links
of a certain format and return them as tuples to be further evaluated

Author: Kai Ellis
date 2020-09-14
"""
import re
import ssl
from bs4 import BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from time import perf_counter_ns

def linkgrab(url): #goes the the target url and extracts all the links that fall under the search conditions. May rework later to have the regex included as one of the options
    # Ignore SSL certificate errors
    #downstart = perf_counter_ns()
    #this part is actually the part that is taking significant time. will need to figureout how to solve this. soupstrainer? 
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = str(urllib.request.urlopen(url, context=ctx).read())
    soup = BeautifulSoup(html, 'html.parser') #converting to string saves 20+ seconds in the nuclear throne wikiread for somereason
    #downfin = perf_counter_ns()
    #print("Page retrival time:", downfin-downstart)
    
# Retrieve all of the anchor tags
#this part appears to actually be o(1)! So no more optimization needed :-) (for now at least)
    #scrapestart = perf_counter_ns()
    tags = soup('a')
    templist = []
    for tag in tags:
        tag = str(tag)
        if re.search(r"^<a href=\"/wiki/[^/]+", tag) and not re.search(r"/wiki/.*[/:].*?\"", tag):
            if re.findall(r"/wiki/(.*?)[\"#]",tag)[0] not in templist:
                templist.append(re.findall(r"/wiki/(.*?)[\"#]",tag)[0])
    #scrapefin = perf_counter_ns()
    #print("Data identification time:", scrapefin-scrapestart)
    return templist    
"""
def linkformat(url,url_intro): #adds on the full url extension, I should also have it remove duplicates while its cycling through
    
    return l
"""
if __name__ == "__main__":
    x = linkgrab("https://en.wikipedia.org/wiki/Battle_of_Ciudad_Ju%C3%A1rez_(1913)")
    print(x)
    print(len(x))
    y = linkgrab("https://en.wikipedia.org/wiki/Ixodes_angustus")
    print(y)
    z = linkgrab("https://en.wikipedia.org/wiki/Battle_of_Waterloo")
    print(z)
    #print(linkformat(x, "https://en.wikipedia.org/wiki/Battle_of_Ciudad_Ju%C3%A1rez_(1913)"))
    

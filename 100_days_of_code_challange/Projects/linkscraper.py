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

def linkgrab(url): #goes the the target url and extracts all the links that fall under the search conditions. May rework later to have the regex included as one of the options
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
    tags = soup('a')
    templist = []
    for tag in tags:
        tag = str(tag)
        if re.search(r"^<a href=\"/wiki/[^/]+", tag) and not re.search(r"/wiki/.*[/:].*?\"", tag):
            templist.append(re.findall(r"/wiki/(.*?)[\"#]",tag)[0])
    return templist    

def linkformat(l): #adds on the full url extension, I should also have it remove duplicates while its cycling through
    for i in range(len(l)):
        l[i] = "https://en.wikipedia.org/wiki/" + l[i]
    return l
if __name__ == "__main__":
    x = linkgrab("https://en.wikipedia.org/wiki/Battle_of_Ciudad_Ju%C3%A1rez_(1913)")
    print(x)
    print(len(x))
    print()
    print(len(linkformat(x)),linkformat(x))

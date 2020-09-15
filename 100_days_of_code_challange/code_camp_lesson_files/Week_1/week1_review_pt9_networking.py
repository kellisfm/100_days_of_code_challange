"""

lots of exercises for this one:
1): modify the socket program to prompt the user for a url of interest that you can connect to
2) change the program so it counts the number of characters and stops displaying text after it's shown 3000. all should be recieved but only 3k printed
3) change the socket program so that it only shows data post header+blank line

note on installing packages with the command line:
format is py -m pip install packagename
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

"""
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #open a server socket, connected to the internet that will stream data
mysocket.connect((host,80)) #connect to a host and port
cmd = f'GET {userl} HTTP/1.0\r\n\r\n'.encode() #issue a command, \r\n\r\n give two carridge returns and two newlines, neccisarry for host recognition
mysocket.send(cmd)

while True: #receives a datastream from the host at port 512(our port), cuts off streaming if there is no data being imported, decodes the html,css,etc
    data = mysocket.recv(512)
    if (len(data) < 1) :
        break
    print(data.decode()) #this converts from UTF-8 to string unicode
mysocket.close() #closes our internet socket
"""

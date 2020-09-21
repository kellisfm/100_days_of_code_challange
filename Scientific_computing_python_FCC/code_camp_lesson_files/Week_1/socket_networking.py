"""
sockets are connections between our computer and a server
python has built in support for tcp sockets in the socket package ex:

import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect( ('hostwebsite.gov'), portnumber)

mostly will receive data in HTTP (hypertext transfer protocol)
set of rules allowing browsers to retreive web documents

typical URL breakdown:
http://www.website.gov/help.htm
protocol       host     document

lets write a web browser:
"""
import socket
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #open a server socket, connected to the internet that will stream data
mysocket.connect(('data.pr4e.org',80)) #connect to a host and port
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode() #issue a command, \r\n\r\n give two carridge returns and two newlines, neccisarry for host recognition
mysocket.send(cmd)

while True: #receives a datastream from the host at port 512(our port), cuts off streaming if there is no data being imported, decodes the html,css,etc
    data = mysocket.recv(512)
    if (len(data) < 1) :
        break
    print(data.decode()) #this converts from UTF-8 to string unicode
mysocket.close() #closes our internet socket

"""
UTF unicode transfer format:
acceptable balance between the higher character count of unicode and the compression of ascii
strings and unicode are identical in python, but bytes of data are weird in the program. Normally this doesnt matter, but when recieving data we need to decode it
or encode it when sending.
"""


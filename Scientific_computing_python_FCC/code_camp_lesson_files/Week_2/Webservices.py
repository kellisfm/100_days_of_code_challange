"""
data on the web: retreiving xml and json files.
these files are designed to be consumed by programs unlike html. this is why beutiful soup mostly just does a hack job of html

Starting with xml:
extensible markup language
xml has similar formatting to html (opening and closing tags)
xml mostly just ignores whitespace

xml schema:
the legal format of an XML document:
identifying whose fault a break was (recieving or sending)


json! 
javascript based, not international standard: some dude just kinda made it in js, and people liked it

"""
import json
data = '''{
    "name": "chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''
info = json.loads(data)
print('name:', info["name"]) # prints name: chuck
print('hide:', info["email"]["hide"])# prints hide: yes

"""
functions very similarly to a python dic or list, unlike xml which is more like html (picky and long)
"""

# other concepts: service oriented approach, API's. Don't actually perform any hard services but do everything that you want (middle man)
# Application programmable interface

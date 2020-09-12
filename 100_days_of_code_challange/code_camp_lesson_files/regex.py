r"""
My boy is back! I love R regex, hopefully python is just as fun.

regex is a concise and flexible way to match and parse strings.

very powerful but hard to learn, ancient programming language

can access with import re

Regex quick guide:
^ beginning of a line
$ end of a line
. anycharacter
\s whitespace
\S non-whitespace
* repeats a character 0+ times
*? non-greedy repeat
+ repeats a char 1+ times
1+ non-greedy
[abcd] matches the first character in the listed set (can include ranges with a-z1-9 etc)
[^abcd] matches the first character not in the listed set
() for extracting characters

example search

hand = open('file.txt')
for line in hand:
    line = line.rstrip
    if re.search('^From: ', line) :
        print(line)
checks to see if each line starts with (^) From:


functions:
re.match() looks for a match at the beginning of the string, results in true/false
re.search() true/false if anything in the string matches the regex
re.findall() extracts any matching strings, returns a list of 0+ matching sub-strings from the og string, will only take from sections in ()! Thats slick
re.split() split string into a list using the delimiter provided
re.compile(pattern) saves a RE style string for further use
Greedy matching: always goes for the longest string, rather than the first one!
use ? if you want first match rather than longer string

extracting an email
"""
import re
handle = open('mbox-short.txt')
for line in handle:
    line.rstrip()
    x = re.findall(r"^From.*@(.*?)\s",line) #find all emails that start with From and go till @, extract all information between @ and the first blank char (thanks to ?)
    if x!= []:
        print(x)

#regex practice 1: Write a Python program to check that a string contains only a certain set of characters (in this case a-z, A-Z and 0-9)
def is_char(String):
    String = re.search(r'[^a-zA-Z0-9]',String)
    return not bool(String)

print(is_char("asdfghjklQWERTYUIOP1234567890"))
print(is_char(r"!@#$%^&_asdfaga"))

#Write a Python program that matches a string that has an a followed by zero or more b's
def is_ab(string):
    string = re.search(r"ab*",string)
    return bool(string)

print(is_ab("abbbbbbbbbbbb"))
print(is_ab("a"))
print(is_ab("ba"))

#Write a Python program that matches a string that has an a followed by zero or one 'b'.
def is_notabb(string):
    string = re.search(r"ab[^b]|a[^b]|a$",string)
    return bool(string)
print(is_notabb("abbbbbbbbbbbb"))
print(is_notabb("a"))
print(is_notabb("ba"))
print(is_notabb("abchdihaf"))
print(is_notabb("bad"))
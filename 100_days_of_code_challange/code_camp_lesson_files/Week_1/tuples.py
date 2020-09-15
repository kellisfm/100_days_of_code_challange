"""
Tuples: based in () , lists [], dict {}

tuples function very similarly to lists, but are immutable (can't be modified) similar to strings!
tuples are more efficient than lists, should always use if you won't need to sort, append or modify in anyway

only functions for tuple:
count()
index()

mostly used for temp variables
lists more for long term use

can put tuples on the left hand side of the assignment variable
ex:
a,b = 1,2

classic use is tuple assignment variable when working with key value pairs in a dictionary:

for k,v in dict.items():
    print(k,v)

Tuples also comparable, goes left to right until one beats the other eg:
(1,2,3,4,5,6) > (1,1,1,1,1,1000000000)
will produce true as 2 is greater than 1 in the second position
similar to how we compare numbers

Sorting tuples:

dict->list of tuples -> sort -> back to dict

can sort in reverse with sorted(data, reverse = True)
"""
d = {"a":2,"b":1,"c":3,"e":0,"d":11}
#method to sort by key:
for k,v in sorted(d.items()):  #takes the dictionary as a collection of tuples, and sorts them by the first value(key)
    print(k,v) #prints

#method to sort by value?
tmp = []
for k,v in d.items():  #takes the dictionary as a collection of tuples
    tmp.append( (v,k) ) #adds each tuple to a list in reverse (value, key) order
print(sorted(tmp)) #sorts based on value!

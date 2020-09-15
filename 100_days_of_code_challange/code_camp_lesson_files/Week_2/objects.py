"""
objects.object() object oriented coding
mostly a terminology section of the course. Seems like the api part was too tbh
Review section for this is gonna be fun

Review of program:
input -> processing -> output
object oriented - program is a series of objects that cooperate to solve the program. program is basically a series of little code islands (allows breaking down of problem)
objects hide detail - allow rest of prgram to ignore the detail within the object

definitions: 
class a template - eg 
method - defined capability of a class - eg a single function within a class
feild - class specific variable
object - an output of a class

class is a reserved word

. is the object lookup operator
so stuff.get() is looking up the get method within the list class
"""
class PartyAnimal: #
    x = 0

    def __init__(self):
        print("I am constructed")
    print(dir(x))
    def party(self):
        self.x +=1
        print("so far", self.x)
    def __del__(self):
        print("i am destructed", self.x)
an = PartyAnimal()

an.party()
an.party()
an.party()
an = 42
print("an contains", an)


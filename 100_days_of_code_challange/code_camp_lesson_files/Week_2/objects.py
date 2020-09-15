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
    name = ""
    def __init__(self,nam):
        self.name = nam
        print(self.name,"constructed")
    print(dir(x))
    def party(self):
        self.x +=1
        print("so far", self.x)





"""
object inheritance: making a new class - can reuse an ixisting class and inherit all the capabilities of that class and add a bit. nother version of store/reuse
classic parent/child = class subclass
"""
class FootballFan(PartyAnimal): #putting in the bracket allows inheritance of all methods
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name,"party count", self.points)
s = PartyAnimal("sally")
s.party()

j = FootballFan("jim")
j.party()
j.touchdown()
"""
boolean expressions:
ask and produce a yes or no answer
t/f
< less than
<= less than equal to
== equal too
>= greater than equal to
> greater than
!= inequal to
if(x==5):
    dont use tabs (errors if you mix tabs and spaces)
can use else : to add in essentially an if == false statement



# multiway branch, for 3+ conditions: If -> elif (1x+) -> else

#example multiway
if(x<2):
    print(small)
if (2 <= x < 20):
    print(medium)
if(x>20):
    print(CHONK)
"""
#try excepts prevent explosions of code and produce something else if an explosion occurs
#never goes back to try block after explosions, make sure only dangerous parts are in try block

""" Exercises:
E1: rewrite the pay code to 1.5x wage if over 40 hours worked

E2: rewrite the pay program using Try except to gracefully handle non-numeric inputs
quit(): ends code, useful for ending out of a try except statement
"""
hour = True
while(hour == True):
    hour = False
    e3hour = input("How long did you work? ")
    try: 
        e3hour = float(e3hour)
    except:
        print("Please enter a number Ex: 1")
        hour = True
print("You worked for", e3hour, "hours.")

pay = True
while(pay == True):
    pay = False
    e3pay = input("What is your hourly wage? ")
    try: 
       e3pay = float(e3pay)
    except:
        print("Please enter a number Ex: 1, or 2.75")
        pay = True

if (e3hour>40):
    print("Overtime bonus! Wages abouve 40 hours multiplied by 1.5x")
    print("you should earn:", 40*e3pay + (e3hour-40)*(e3pay*1.5))
else:    
    print("you should earn:", e3hour * e3pay)

    #testing for git changes
    
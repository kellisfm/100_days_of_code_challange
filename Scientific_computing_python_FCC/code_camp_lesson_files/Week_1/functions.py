"""
def help():
    code
    code
    code
def will not run the code, it just remebers it and will invoke it whenever you run the named code
really useful for long stretches of code that you don't want to have to type or correct over and over again

Two types: defined and built in

example functions: max(letters) returns the 'highest' lowercase letter in the string that you input
min() does the opposite

building our own functions:
def function_name(parameter 1, parameter 2)
parameters are variables that are used in the function defition, it is a way to allow the code to access the arguments in a particular function arrangement

return: ends the function (like break) and specifies the output of the function
"fruitful" functions return a result or value
"""
#exercise: rewrite your compute pay script into a computepay(hours, rate) function
def computepay(hours, rate):
    
    try: 
        phours = float(hours)  
    except:
        print("Please enter hours as an integer Ex: 1")
        quit()

    try: 
        prate = float(rate)
    except:
        print("Please enter rate as an integer Ex: 1, or 2.75")

    if (hours>40):
        
       pay = 40*prate + (phours-40)*(prate*1.5)
    else:
        pay = phours * prate    
    return pay 


xp = computepay(45,2)
print(xp)
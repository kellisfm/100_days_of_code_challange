#the following exercises were taken from the exercise portion of the PY4E textbook, available at: http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf
#exercise 4: what do the following statements produce
width = 17
height = 12.0

print(width//2) #8, closest whole devisor
print(width/2.0) #8.5
print(height/3) #4.0 always converts to float when deviding
print(1+2*5) # 11, bedmas

#write a program which asks for a celcius temp, convert to fahrenheit and print

run = True

while run == True:
    cel = input("What temperature in celcius would you like to know in farenheit? ")
    try:
        cel = float(cel)
    except:
        print("please enter a number")
        continue
    far = (cel * 9/5) + 32 
    print("Your temperature in degrees F is:", far)
    passs = False
    while passs == False:    
        run = input("would you like to go again? Enter True or False:" )
        if run in ["True","False"]: #lesson for the future here bool() only checks if the string is not empty! This doesnt function like string, int or float. this list if statement 
            #functions as a checker to ensure the user entered the boolean values True or False, while the next line converts from string to bool
            run = run == "True"
            passs = True
        else:
            print("enter True or False")
        
        
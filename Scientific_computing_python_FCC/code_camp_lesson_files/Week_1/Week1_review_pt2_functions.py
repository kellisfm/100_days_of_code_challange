"""
write a program to prompt for a score between 0.0 and 1.0
if the score is outside of this range, print an error. Else print a grade using the following table:
    A >= 0.9
    B >= 0.8
    C >= 0.7
    D >= 0.6
    F <0.6
"""
def gradeconverter(gradefloat):
    if(gradefloat) >= 0.9:
        return("A")
    if(gradefloat) >= 0.8:
        return("B")
    if(gradefloat) >= 0.7:
        return("C")
    if(gradefloat) >= 0.6:
        return("D")
    if(gradefloat) < 0.6:
        return("F")

run = True
while run == True:
    gradepercent = input("please enter your grade as a decimal (Between 0.0 for totally wrong and 1.0 for perfect.) ")
    try:
        gradepercent = float(gradepercent)
        if not 1.0 >= gradepercent >= 0.0:
            print("Please enter a number between 0.0 and 1.0")
            continue
    except:
        print("Please enter a number!")
        continue
    grade = gradeconverter(gradepercent)
    print("Your letter grade is:", grade)
    passs= False
    while passs == False:    
        run = input("would you like to go again? Enter True or False:" )
        if run in ["True","False"]: #lesson for the future here bool() only checks if the string is not empty! This doesnt function like string, int or float. this list if statement 
            #functions as a checker to ensure the user entered the boolean values True or False, while the next line converts from string to bool
            run = run == "True"
            passs = True
        else:
            print("enter True or False")


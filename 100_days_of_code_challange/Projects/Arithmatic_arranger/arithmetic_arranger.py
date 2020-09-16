"""
function:
arithmetic_arranger:
takes a list with up to five entries of "number +- number"
prints them in columns formatted according to the specifications found in proj_desc.txt

Author: Kai Ellis
Date: 2020-09-16
Tomorrow i need to figure out how to use the .format function
"""

def arithmatic_arranger(l,tf = False):
    if len(l) > 5: #check to see if there are more than five problems entered
        print("please enter five or less problems")
        quit()
    count = 0 #this will enable ease of user troubleshooting
    for entry in l: #split all the problems into their component parts
        entry = entry.rstrip()
        entry = entry.lstrip()
        entry = entry.split()

        if len(entry)!= 3: #make sure the problems have been submitted as two numbers and an operator seperated by spaces
            print("Problem", count+1, "is misformatted, please enter as: number + or - number")
        if len(entry[0]) > 4 or len(entry[2]) > 4: #check 4 digit max
            print("Problem", count+1, "has a number greater than 4 digets long, please reduce length")
            quit()
        print(entry)
        l[count] = entry
        l[count].append(len(max(l[count],key = len)))
        count += 1
    print(l)
    toprow = "\t"
    bottomrow = ""
    for entry in l: 
        toprow += ("{:<0}{1}\t".format(entry[0]))
    print(toprow)
    print("done")
if __name__ == "__main__":
    
    x = ["1512 + 5", "2 + 2","52 - 21", "162 - 5"]
    arithmatic_arranger(x)

"""
function:
arithmetic_arranger:
takes a list with up to five entries of "number +- number"
prints them in columns formatted according to the specifications found in proj_desc.txt

Author: Kai Ellis
Date: 2020-09-16
"""
import re
def arithmetic_arranger(l,tf = False):
    if len(l) > 5: #check to see if there are more than five problems entered
        return("Error: Too many problems.")

    count = 0

    for entry in l: #this loop splits the entry into its component parts, allowing us to test for entry errors, and enabling further string manipulation
        
        entrylist = entry.split()

        if len(entrylist[0]) > 4 or len(entrylist[2]) > 4: #check 4 digit max
            return "Error: Numbers cannot be more than four digits."

        if not re.match("[+-]",entrylist[1]): #check to see if they have entered an operator other than +-
            return "Error: Operator must be '+' or '-'."

        if re.search(r"\D", entrylist[0]) or re.search(r"\D", entrylist[2]): #confirm there are only diget characters
            return "Error: Numbers must only contain digits."

        l[count] = entrylist #enter the now broken down equation into the list
        l[count].append(len(max(l[count],key = len))) #longest number's length, saved for future formatting use

        if tf == True: #checks if they want an answer, provides if yes
            l[count].append(eval(entry))

        count += 1

    toprow = ""
    bottomrow = ""
    line = ""
    answerline = ""
    for entry in l: #runs through each problem entry and formats them by parts (top number, bottom number, line, and potentially answer)
        indent = ">" + str(entry[3])
        toprow += ("  " + format(entry[0],indent) + "    ")
        bottomrow += ( entry[1] + " " + format(entry[2],indent) + "    ")
        line += "-"*(entry[3] + 2) + "    "

        if tf == True: #formats the answer, if desired
            ansindent = ">" + str(entry[3]+1)
            answerline += " " + format(entry[4],ansindent) + "    "

    finreturn = (toprow.rstrip() + "\n" + bottomrow.rstrip() + "\n" + line.rstrip()) #merge the component parts into one final answer string

    if tf == True: #add answer if neccissary
        finreturn += ("\n" + answerline.rstrip())
    
    return finreturn #return final format

if __name__ == "__main__":
    x = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49"]
    print(arithmetic_arranger(x, True))

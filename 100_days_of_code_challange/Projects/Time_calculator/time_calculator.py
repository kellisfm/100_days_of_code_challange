"""
function:
add_time( start,duration,day(optional) ):
start is a time in 12 hour format ending in am or pm
duration is a time in the form of hours and minutes
day is an optional argument and indicates the starting day

return: adds the duration time to the start time. If the result will be one day later, it should show "next day" after the time.
> 1 day later, should show "n days later" where n is the number of days
if the day is given, it should give the day that it lands on.

Other rules:
no libraries allowed, assume the start time is always valid
Author: Kai Ellis
Date: 2020-09-16
"""

def add_time(start, duration, day = None):
    #Start off by breaking the clocks down into the component parts of hours/minutes
    start = start.split()
    time = start[0].split(":")
    duration = duration.split(":")

    #convert from string to int
    time = [int(i) for i in time] 
    duration = [int(i) for i in duration]

    #add duration to time for the hour and minute parts
    finmin = time[1] + duration[1]
    finhour =  time[0] + duration[0]

    #convert to 24 hour time for ease of future math
    if start[1] == "PM":
        finhour += 12

    # we can use the // (highest clean divisor), and modulus functions to understand weather an extra day/hour has passed, and to get the final time on the next day respectively
    finhour += finmin//60
    finmin = finmin%60

    if len(str(finmin)) == 1: #modulus will return the fewest number of digits, we have to add an extra 0 where neccisary
        finmin = f"0{finmin}"
    
    finday = finhour//24
    finhour = finhour%24

    print(finhour)

    if (finhour-12) == 0: # because the clock roles over at 12, and modulus gives a instead of 24 at 24 we have to account for a couple of extra cases
        fintime = f"12:{finmin} PM"
    elif finhour == 0: 
        fintime = f"12:{finmin} AM"
    else: #convert to AM if the time is lower than 11
        if finhour <= 11:
            fintime = f"{finhour}:{finmin} AM"
        else: #PM if 12 or higher
            fintime = f"{finhour - 12}:{finmin} PM"
    if day != None: #add day if given
        date_dic = {"monday":1,"tuesday":2,"wednesday":3,"thursday":4,"friday":5,"saturday":6,"sunday":7}
        day = (date_dic[day.lower()] + finday) % 7
        if day == 0: #correcting for modulus 
            day = 7
        day = [k for k,v in date_dic.items() if v == day][0] #using dictionary comprehension to extract key from value
        fintime += (", " + day.capitalize())
    
    if finday > 0: #add how many days have passed, 3 options: no days, 1 day, or more than 1 day
        if finday == 1:
            fintime += " (next day)"
        else:
            fintime += f" ({finday} days later)"
        
    return fintime



if __name__ == "__main__":
    x = ()
    print(add_time("11:59 AM", "24:05"))

    (6+12+205)//24
"can calculate, by doing // to find the number of days passed and % to find the number of hours pushed"
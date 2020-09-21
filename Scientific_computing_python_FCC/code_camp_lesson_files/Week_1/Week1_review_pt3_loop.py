#write a program that repeatedly reads numbers until the user enters done, once done is entered print out total, count, average, max and min. Error messages should appear on error
count = 0
maxi = None
mini = None
total = 0
while True: #Don't need a variable as there is alread a breakpoint
    inp = input("Keep entering numbers to receive the total, number count, number average, max number and min number, enter done to recieve your final total: ")
    if inp == "done":
        break
    try:
        inp = float(inp)
    except:
        print("please enter a number or done")
        continue
    count += 1
    total += inp
    if maxi == None or inp > maxi:
        maxi = inp
    if mini == None or inp < mini:
        mini = inp

average = total/count

print("Count: %g" %count,"Total: %g"%total,"Average: %g" %average,"Maximum: %g" %maxi, "Minimum: %g" %mini, sep = "\n")


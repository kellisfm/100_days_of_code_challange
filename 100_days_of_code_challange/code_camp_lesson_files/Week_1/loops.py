"""
LOOOOOPS:
teaching computers to repeat things, again and again and again

Two loops in this course: while and for

While loops basically act like a repeating if statement, need a repeating variable
that prevents the loop from running forever. ALL LOOPS NEED AN EXIT!

example:
n = 0
while True:
    if n == 3:
        break
    print(n)
    n = n + 1
runs until n becomes 3, output is:
0
1
2

example infloop
n=T
while n==T:
    print(INFLOOP)
no way to leave hahaha

indefinite loops: while loops can be indefinite as they have a less defined run time

breaking loops:
break statement, jumps to the next statement, can use for multiloop programs
return: gives an output and then breaks
continue: jumps to the next iteration, but keep in the loop

For loops: definite, deal with a preprocessed list, more likable than while
most of the time

ex:
for i in [5,4,3,2,1] :
    print(i)
print("BLASTOFF!")

Notice the defined range given to the for list

friends = ['kai', 'isaac', 'marc']
for s in friends:
    print(s)

for loops: first check if done, then move i ahead, then perform operations
then retest

loop idioms: getting into sorting algorithms

Pattern for loops: knowing something about the code that you can do by
impacting the data one at a time

"""
largest = 0
count = 0
summ = 0
#grabs largest
for i in [1,12,17,27,11,55,34,90,8]:
    if i>largest:
        largest = i
    count = count + 1
    summ = summ + i

average = summ/count
print(largest, count, summ, average)
"""counting in a loop:
to count how many times a loop is executed, we introduce a counter variable
that starts at 0 and adds one to it each time we run through the loop

search in list, can use boolean to go until the thing is found
example search
"""
found = False
for i in [1,12,17,27,11,55,34,90,8]:
    if i == 11:
        found = True
        break
    print(found, i)
print(found)

#grabs smallest
smallest = None
for i in [1,12,17,27,11,55,34,90,8]:
    if smallest == None or i < smallest: #note that =="str" has to come first, as you can't compare i to the string in the first run
        smallest = i
    count = count + 1
    summ = summ + i
print(smallest)

"""
is is a souped up ==, it looks at type as well as value, should only use for boolean and none
is not is a souped up !=, functions the same way as is
"""
# exercise: write a program which repeatedly reads numbers until the user enters done, once done is entered, print the total, count and average of the numbers, 
# make sure non-int/floats do not break the setup
total = 0
count = 0
while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    
    try:
        number = float(number)
    except:
        print("please enter a numeric character")
        continue
    total = number + total
    count = count + 1

print(total, count, total/count)

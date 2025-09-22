# EH 6th Time and For Loops notes

import datetime

current = datetime.datetime.now()
hour = current.hour

#print(f"The time in seconds since Jan, 1 1970 is {epoch}")
print(f"The current time is: {current}")
print(f"The hour is {hour}")

# Lists - store multiple pices of information in one varilable. Surrounded by straight brackets. Must all be correct datatype.
siblings = ["Eliza", "Valerie", "Henry", "Lilly", "Luna", "Zara", "Juno"]

print(siblings[0])
print(siblings)
#siblings[4] = "Luna Lovegood"
#siblings.remove ("Juno")
#siblings.remove ("Zara")
#print(siblings)

#What is a loop? A loop will keep going until a specific condition is met.
#What are the two types of loops? For loops and While loops

#For loop
for sibling in siblings: #"sibling" is a temporary variable. It has to match the reference.
    print(f"Hello, {sibling}")
    #print("HI") # does it for each one even if it's not using them in the output.

for x in range(20,0, -1): #start, stop, optional: what we count by. stops on one before the stop number.
    print(x)

#While loops
#1. Iterator: keeps track of how many times the loop has run.
#2. End condidiotn: tells the loop when to stop.
#3. Increase the iterator.

#Infinite loop (bad)
#while True:
    #print("Oh no!")

#Good while loop
i = 1 #use i for iterator

while i < 21:
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
    i += 1

import random

number = random.randint(1,20)
x = 1

'''while x != number:
    print("Duck")
    x += 1

print("Goose!")'''

while True: #while True loops usually need a break
    if number == x:
        print("Goose!")
        break #breaks the loop
    else:
        print("Duck")
        x += 1

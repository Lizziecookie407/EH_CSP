#EH 6th Conditionals Notes

#What puts something inside of the “if” statement? The tabbed information below it is inside.
#What do if statements do? Checks for a true or false statement. It will run if it is true.
#What are boolean statements? After the "if", the thing that is either true or false.
#What do else statements do? they are a catch all to complete an action if the statement is not true.
#What kind of statement do you use if you have more than 2 needed outcomes? elif
#What do each of the different symbols mean in conditionals?
# < less then, if the first thing is less then the second thing
# > greater than
# <= less then or equal to
# >= greater than or equal to
# == equal to (we use two equal signs so it doesnt think we are setting a variable)
# != not equal to (! means not)
#What are the 3 logical operators?
#What are logical operators for?
#What does a nested conditional statement do?

num = int(input("Give me a number: "))

if num < 10: # boolean statement or condition
    print(f"{num} is a single digit number.")
elif num < 100:
    print(f"{num} is a double digit number.")
elif num == 18:
    print("That is the winning number!")
else:
    print(f"{num} is a big number!")


name = input("What's your name: ")

if name == "ELIZA":
    print("You are welcome here.")
elif name == "Tia": # checks another thing before going to the else statement (also after the first if statement)
    print("You are a random person related to Mrs LaRose!")
else:
    print("You are not welcome here.")

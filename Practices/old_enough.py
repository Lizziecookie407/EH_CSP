#EH 6th Old Enough 

age=int(input("Your age (in years): "))

if age >200:
    print("Wow, I don't know how you're still alive to type this! (But you can also vote. Congratulations!)")
elif age >=18:
    print("You are old enough to vote!")
elif age >=16:
    print("You are old enough to drive!")
elif age >=15:
    print("You are old enough to get a learners permit!")
elif age >=4:
    print("You are old enough to go to school!")
else:
    print("Wait until you are a little older!")
#EH 6th Time of day

time=int(input("What is the hour in military time: "))

if time >= 0 and time <= 4:
    print("Good morning...")
elif time >= 5 and time <= 11:
    print("Good morning!")
elif time >11 and time <= 16:
    print("Good afternoon!")
elif time >=17 and time<=24:
    print("Good evening!")
elif time > 24:
    print("Hey you, enter a valid time!")
else:
    print("Good day!")
# EH 6th Strings notes

print("I did it!")

#What makes something a string? a string is a collection of symbols that are held together by quotation marks or single quotes. both sides of quotes have to match.
#Why do we have strings? giving information, user inputs, words
#How do stupid proofing and sanitization relate to each other? users=stupid
#What is debugging? debudding is fixing problems in my code.
    #a bug is any error in the code that keeps it from running or makes it run imporperly.
#How do you debug the different types of errors?
#Describe what each of the methods below does:
    #find() tells us the index of where something is
    #concatenate (add) puts things right next to each other exactly as they are. use + (instead of comma)
    #upper() and lower() makes all letters that case. if you do both the last one is what happens
    # #strip() gets rid of spaces at begining and at the end
# Syntax Error: whne you write the code wrong so the computer can't read it. if you run the code with a syntax error then it will tell you and where.
    #use the wrong quotation marks in a string. forgeting an equal sign, comma, plus, or parentheses.
# Logic error: where the code does something that you didn't expect it to do. this is not a problem with the structure but the steps to complete the process.
# Run-Time Error: a problem in the code that will cause it to break when/while the code runs.
    # Mispelling variables. incorrect user inputs.

#examples of strings
first_name=input("What's your first name? ").strip().lower().title()
last_name=input("What's your last name? ").strip().lower().title()
full_name=first_name+" "+last_name
sentance="the quick brown fox jumps over the lazy dog."
print("Welcome to my program", full_name+"!")

    #errors
#syntax error
string= 'this is my string'
#Logic error
num_one=1
num_two=3
print(num_one + num_two) # does not do addition, jsut puts them together
#run code error
letter= "1" # "a" cant make a letter a number
int(letter)

print(sentance.find("brown"))
print(sentance[4:10])
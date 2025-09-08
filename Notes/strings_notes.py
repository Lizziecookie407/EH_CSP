# EH 6th Strings notes

print("I did it!")

#What makes something a string? a collection of symbols that are held together by quotation marks or single quotes. both sides have to match.
#Why do we have strings? giving information, user inputs, words
#How do stupid proofing and sanitization relate to each other? users=stupid
    #strip gets rid of spaces at begining and at the end
    #.upper and .lower makes all letters that case. if you do both the last one is what happens
#Concatination: puts things right next to each other exactly as they are. use + (instead of comma)
#What is debugging?
#How do you debug the different types of errors?
#Describe what each of the methods below does:
    #find()
    #concatenate (add)
    #upper()
    #lower()
    #strip()

#examples of strings
first_name=input("What's your first name? ").strip().lower().title()
last_name=input("What's your last name? ").strip().lower().title()
full_name=first_name+" "+last_name
sentance="the quick brwon fox jumps over the lazy dog."
print("Welcome to my program", full_name+"!")
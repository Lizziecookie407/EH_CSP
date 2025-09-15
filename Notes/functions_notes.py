#EH 6th Functions Notes

import random

#A function is: a set of inctructions that are executed when you use a keyword. not based on a spesific data type.
#Why we use functions: To simplify and shorten code. For when you want the same thing to happen over and over again with different information. So we don't have to rewrite code.
#White space: used to tell computers where things are (indents). the tabs you are using must match to keep your code from breaking.
#Parameters and arguments are: Paramenters go inside the parenthases when defining the funtion. Arguements are when you call the funtion.

#Return statements are
#How to use return statements in a program

#How we write funtions
print("this")

#Creating a function
def welcome():
    name=input("What is your name?\n")
    print(f"hello {name}")

print("The function is over.")

#calling a function
#welcome()

#parameters and arguments
def add(number, number_two): #parameters
    number=number + number_two
    print(number)
#number exists only in the function
num_one=12
num_two=14
add(num_one,num_two) #arguments
add(4,8)
add(9,70)
add(87,45)

def clean(info):
    return info.strip().lower()

name=input("What is your name?\n")
quest=input("What is your quest?\n")
color=input("What is your favorite color?\n")

print(f"Hello, {clean(name)}. I have heard you are trying to {clean(quest)}, that is super cool! Are you sure {clean(color)} is your favorite color?")

def believe(sentence):
    length = len(sentence)
    spot_one= random.randint(0,length-1)
    spot_two= random.randint(0,length-1)
    spot_three= random.randint(0,length-1)
    full_sentence = sentence.split(" ")
    full_sentence.insert(spot_one, "Beleive it!")
    full_sentence.insert(spot_two, "Beleive it!")
    full_sentence.insert(spot_three, "Beleive it!")
    sentence= " ".join(full_sentence)
    return sentence

new_sentence= believe("The quick brown fox jumped over the lazy dog!")
print(new_sentence)
print(believe("Peter Piper picked a peck of pickled peppers."))

#EH 6th Expressions Notes

#What is an algorithm? 
    #A set of instructions to amcomplish a task. it will work every time and do the exact same steps.
#List steps in an algorithm: 
    #1) determine what variables/peices of into you need. 2) prosesses info. 3) provide output.
#List ALL of the different mathematical operators (Give me the symbol and tell me what it does)
    #+ add, - subtract, * multiply, / devide, ** exponents, //integer division, % modulo(remainder) 
#List ALL of the different assignment operators (Give me the symbols and what it does)
#Why are expressions so important in programming?
    #because if you set it up once, you never have to do it again. lazyness in advance. Long term.
# an expressison is a collection of numbers and symbols that get a result.
# integer is a data type that can hold whole numbers. can be negitive.
# float is short for floating-point number and holds decimals. 

name=input("What is your name? ")
print("Hello,",name,"!")

#algorithm for area
length=5
width=20
area= length * width
print("\n",length, "X", width, "=", area)

#step 1
age1=14
age2=14
age3=15
age4=15
#step 2
average= (age1+age2+age3+age4)/4
#step 3 
print("\nThe average of", age1, ",", age2, ",", age3, ", and", age4, "is", average, ".")

#math equations/assignment operators
num_one =  float(input("Give me a number:\n"))
num_two = int(input("Give me a number:\n"))

num_one += num_two
print("\naddition (+):",round(num_one, 0)) #Rounding: 1. what needs rounded 2. by how manyhg
num_one -= num_two
print("subtraction (-):",num_one)
num_one *= num_two
print("multiplication (*):",num_one)
num_one /= num_two
print("devision (/):",round(11/3, 0))
num_one **= num_two
print("exponents (**):",num_one)
num_one //= num_two
print("integer division (//):", num_one)
num_one %= num_two
print("modulo (remainder) (%):",num_one)

print("\n(3*5**2/15)-(5-2**2)=",(3*5**2/15)-(5-2**2))
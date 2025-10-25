import random

ajz = []
f_ajz = []
n_ajz = []
num = 0
q = 0

def ifrepeat(num):
    numstr = str(num)
    numstrset = set(numstr)
    return len(numstr) > len(numstrset)

def com_play(guess):
    numstr = str(num)
    for digit in str(guess):
        if digit in numstr:
            ajz.append(2)
        else:
            ajz.append(3)
    ajz.sort()

    if "".join(str(ajz)) == "111":
        q = 1
    else:
        q = 0

    for digit in ajz:
        if digit == 1:
            f_ajz.append("A")
        elif digit == 2:
            f_ajz.append("J")
        elif digit == 3:
            f_ajz.append("Z")
        else:
            continue

    return f_ajz

def guess():
    output = ["  "]
    guess = input(": ").strip()
    f_ajz = com_play(guess)
    output += str(guess)
    output += " | "
    output += f_ajz
    output = "".join(output)
    print(f"\r{output}")
    output = []

i = 0
while i < 1:
    num = random.randint(102,987)
    print(num)
    if ifrepeat(num) == True:
        print("has repeat")
        i = 0
    else:
        print("has no repeat")
        i = 1

print("\nHow to play:\n1) Guess a 3 digit number with no repeating digits.\n2) The computer will give an output with a comination of A, J, and Z.\n3) A indicates that a letter is correct and placed in the correct spot.\n   J inticates that a letter is correct, but in an incorrect position.\n   Z indicates that a letter is incorrect.\n4) Use this key to guess numbers until you find the right one.\nHave fun!")
print("\n  ### | AJZ")

while q < 1:
    guess()
    ajz = []
    f_ajz = []
print("You guessed it!")
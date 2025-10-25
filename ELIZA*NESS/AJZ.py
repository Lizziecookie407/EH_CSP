import random

ajz = []
f_ajz = []
n_ajz = []
num = 0
q = 0
guess_count = 1

def ifrepeat(num):
    numstr = str(num)
    numstrset = set(numstr)
    return len(numstr) > len(numstrset)

def com_play(guess):
    numstr = str(num)
    guestr = str(guess)
    r = 0
    for digit in guess:
        if guestr[r] == numstr[r]:
            ajz.append(1)
            r += 1
        elif guestr[r] in numstr:
            ajz.append(2)
            r += 1
        else:
            ajz.append(3)
            r += 1
    r = 0

    ajz.sort()

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
    output = [""]
    guess = input(" : ").strip()
    if len(guess) < 3 or len(guess) > 3:
        print(f"{guess_count}| Guess three digits.")
        return
    f_ajz = com_play(guess)
    output += str(guess)
    output += " | "
    output += f_ajz
    output = "".join(output)
    print(f"{guess_count}| {output}")
    output = []

i = 0
while i < 1:
    num = random.randint(102,987)
    #print(num)
    if ifrepeat(num) == True:
        #print("has repeat")
        i = 0
    else:
        #print("has no repeat")
        i = 1

print("\nHow to play:\n1) Guess a 3 digit number with no repeating digits.\n2) The computer will give an output with a comination of A, J, and Z.\n3) A indicates that a letter is correct and placed in the correct spot.\n   J inticates that a letter is correct, but in an incorrect position.\n   Z indicates that a letter is incorrect.\n4) Use this key to guess numbers until you find the right one.\nHave fun!")
print("\n   ### | AJZ\n   ---------")

while True:
    if ajz == [1,1,1]:
        print("Great job, you guessed it!\nRerun the code to play again.")
        break
    else:
        guess_count += 1
        ajz = []
        f_ajz = []
        guess()
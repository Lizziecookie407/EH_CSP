#EH 6th Silly Sentances

print("Hello and welcome to my silly sentance generator!")

word_one=input("Give me an animal: ").strip().lower()
word_two=input("Give me a food item: ").strip().lower()
word_three=input("Give me a noun: ").strip().lower()
word_four=input("Give me a verb (ending in -ing): ").strip().lower()

print("\nHere is your silly sentance!")
print("If you give a "+word_one+" a "+word_two+", then it will ask you for a "+word_three+".")
print("If you give the "+word_one+" a "+word_three+", then you'll have to go "+word_four+" with them.")
print("And before you know it, you'll be "+word_four+" while eating a "+word_two+" with a "+word_one+"!")
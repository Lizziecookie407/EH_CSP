// EH 6th Silly Sentences

#include <stdio.h>

int main(void){

    char word_one[20];
    char word_two[20];
    char word_three[20];
    char word_four[20];

    printf("Hello and welcome to my silly sentance generator!");

    printf("\nEnter an animal: ");
    scanf("%s", word_one);
    printf("Enter an food item: ");
    scanf("%s", word_two);
    printf("Enter an noun: ");
    scanf("%s", word_three);
    printf("Enter an verb (ending in -ing): ");
    scanf("%s", word_four);

    /*word_one=input("Give me an animal: ").strip().lower();
    word_two=input("Give me a food item: ").strip().lower();
    word_three=input("Give me a noun: ").strip().lower();
    word_four=input("Give me a verb (ending in -ing): ").strip().lower();*/

    printf("\nHere is your silly story!");
    printf("\nIf you give a %s a %s, then it will ask you for a %s.", word_one, word_two, word_three);
    printf("\nIf you give the %s a %s, then you'll have to go %s with them.", word_one, word_three, word_four);
    printf("\nAnd before you know it, you'll be %s while eating a %s with a %s!\n", word_four, word_two, word_one);
    
    return 0;
}
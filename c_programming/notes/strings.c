// EH 6th Strings Notes
/*
What is the difference between a string and a character?
 a string is a list of characters
What types of quotation marks do we need for a string?
 '' for single characters, "" for more than one character, (strings)
What library do we need to include to access the string functions in C?
 #include <string.h>;
List functions the library allows us to use.
 strcat() strleng() sizeof()
How do we concatenate strings in C?
strcat()
How do we get individual characters from a string in C?
name[#]
*/

#include <stdio.h>
#include <string.h>

int main(void){
    char name[100] = "Valerie"; // can leave brackets blank if you define it, need to make it bigger if you are going to add things to it by concatinating
    char last_name[25]; // must have a character limit because it's not defined, so the space is saved
    char full_name[100];

    printf("Enter your last name: ");
    scanf("%s", &last_name);

    printf("\n[%s]", name);
    strcat(name, " ");
    strcat(name, last_name);
    printf("\n[%s]", name);
//you can concatonate strings into empty variables
    strcat(full_name, name);
    printf("\n%s", full_name);

    return 0;
}
// EH 6th Name Decorator

#include <stdio.h>
#include <string.h>

int main(void){
    char name[30];
    char first[] = "|^|~";
    char last[] = "~|^|";

    printf("Enter your name: ");
    scanf("%s", name);

    strcat(name, last);
    strcat(first, name);
    printf("\nHere is your decorated name!\n%s\n", first);
    
    return 0;
}
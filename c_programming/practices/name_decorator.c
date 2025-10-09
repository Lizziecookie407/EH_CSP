// EH 6th Name Decorator

#include <stdio.h>
#include <string.h>

int main(void){
    char name[20];
    printf("Enter your name: ");
    scanf("%s", &name);
    strcat(name, "~|^|");
    strcat("|^|~", name);
    printf("\nHere is your decorated name!\n%s", name);
    
    return 0;
}
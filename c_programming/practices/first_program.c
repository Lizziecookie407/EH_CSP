// EH 6th First Program

#include <stdio.h>

int main(void){
    char name[20];
    printf("\nWhat is your name: ");
    fgets(name, sizeof(name), stdin);
    printf("Hello, %s! Nice of you to run my code.", name);

    return 0;
}
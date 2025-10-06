// EH 6th First Program

#include <stdio.h>

int main(void){
    int name;
    printf("\nWhat is your name: ");
    fgets(name, sizeof(name), stdin);
    printf("Hello, %c", name);

    return 0;
}
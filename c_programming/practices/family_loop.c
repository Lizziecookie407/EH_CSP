// EH 6th

#include <stdio.h>

int main(void){

    char family[7][20] = {"Mommy", "Daddy", "Eliza", "Valerie", "Henry", "Lilly", "Luna"};

    for(int i = 0; i < 7; i++){
    printf("Hello, %s!\n",family[i]);
    }
    return 0;
}


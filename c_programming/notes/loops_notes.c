// EH 6th Loops amd Arrays Notes
/*
What is a loop? 
 something that repetes when you tell it to, with iterators
What are the two types of loops?
 for loop and while loop
What is iteration?
 a number counting a amount of times you loop
What are arrays? 
 a collection of data grouped together (a list)
*/


#include <stdio.h>

int main(void){
/*
    char *fruits[] = {"apple", "banana", "cherry"};
    int num_fruits = sizeof(fruits) / sizeof(fruits[0]);

    for(int f 1 = 0; f < num_fruits; f++){
        printf("I like %s!\n",fruits[f]);
    }
*/
    //list or array
    int nums[10] = {1,2,3,4,5,6,7,8,9,10}; //must set data type, braces instead of brackets, commas
    char candy[5][20] = {"Skittles", "Butterfinger", "Reese's", "Kit Kat", "Twix"};

    //for loops
    for(int x = 0; x < 10; x++){
        printf("%d\n", nums[x]);
    }

    for(int i = 0; i < 5; i++){
    printf("%s is my favorite candy!\n", candy[i]);
    }

    for(int num =1; num <11; num++){
        printf("%d\n", num);
    }

    //while loop
    int goose = 6;
    int count = 0;
    while(count != goose){ //only difference from python is the parenthases and braces
        printf("Duck\n");
        count++;
    }
    printf("Goose!");
    
    return 0;
}
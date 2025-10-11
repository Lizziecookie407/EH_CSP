// EH 6th Old Enough

#include <stdio.h>

int main(void){
    int age;
    printf("Enter your age (in years): ");
    scanf("%d", &age);

    if(age >=200){
    printf("Wow, I don't know how you're still alive to type this! (But you can also vote. Congratulations!)");
    }else if(age >=18){
    printf("You are old enough to vote!");
    }else if(age >=16){
    printf("You are old enough to drive!");
    }else if(age >=15){
    printf("You are old enough to get a learners permit!");
    }else if(age >=4){
    printf("You are old enough to go to school!");
    }else if(age < 0){
    printf("Wait until you're born sweetie.");
    }else{
    printf("You have your whole life ahead of you!");
    }

    return 0;
}
// EH 6th Time of Day

#include <stdio.h>

int main(void){
    int time;
    printf("What is the hour in military time: ");
    scanf("%d", &time);

    if(time >= 0 && time <= 4){
    printf("Good morning...");
    }else if(time >= 5 && time <= 11){
    printf("Good morning!");
    }else if(time >11 && time <= 16){
    printf("Good afternoon!");
    }else if (time >=17 && time<=24){
    printf("Good evening!");
    }else if(time > 24 || time < 0){
    printf("Hey you, enter a valid time!");
    }else{
    printf("Good day!");
    }
    return 0;
}
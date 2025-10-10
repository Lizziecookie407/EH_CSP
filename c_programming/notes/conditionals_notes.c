// EH 6th Conditionals Notes
/*
What puts something inside of the “if” statement?
 braces/curly brackets {}
How are conditions written in C?
 if(conditional) { 
 }else if(conditional) { 
 }else(conditional) {}
How do we write elif conditions in C?
 use else if instead of elif
When do else conditions run?
 after checking all the if and elif statments and when nothing else applies
What are the 3 logical operators in C?
 && and
 || or
 ! not

 < less than
 > greater than
 <= less than or equal to
 >= greater than or equal to
 == equal to
 != not equal to
*/


#include <stdio.h>
#include <string.h>

int main(void){
    int grade;
    char name[50];
    printf("What is your grade?: ");
    scanf("%d", &grade);
    printf("What is your name: ");
    scanf("%s", &name);

    //you cant compare strings with opperators
    printf("%d\n", strcmp(name, "Ms. LaRose"));

    if(strcmp(name, "Ms. LaRose")==0){
        printf("You don't have a grade!\n");
    }

    if(grade > 90){ //goes inside parentheses
        printf("You have an A.\n");
    }else if (grade >=80){ // use else if instead of elif
        printf("You have a B.\n");
    }else{
        printf("You do not have an A.\n");
    }
    
    return 0;
}
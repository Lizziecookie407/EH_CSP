// EH 6th Variables Notes
#include <stdio.h>

/*What is the main difference between declaring variables in Python and C?
 must state what type of information the variable will hold - static data type
In C, what is the purpose of specifying a data type when declaring a variable?
 saving memory. it has a specific number of bytes.
 int 4 float 4 double 8 char 1, bytes. char - list of characters for a string
List three common data types used in C and their corresponding format specifiers for printf().
 char=c string=s digit=d float=f double=
What is the difference between printf() and scanf() functions in C?
 printf still prints a statment but scanf will take in something as an imput */
//How do you add comments in C?
/*this 
will remain a comment
even on a different line
*/
/*What is the purpose of the #include <stdio.h> line at the beginning of a C program?
 takes in the standard liberary input/output
In C, what is the significance of the main() function?
 it sets up the way to have variables and the void means nothing is changed
What is the difference between %d and %f format specifiers in printf()?
 %d is a place holder for a digit, one number, and %f is a place holder for a float, a number including a decimal point
How do you print a newline character in C?
 \n
What is the purpose of the & symbol when using scanf() to get user input?
 it is basically the += symbol and means it adds it to the variable named
How do you declare a constant in C?
 put const in front of the variable type
*/

int main(void){
    int num = 4;
    const float pi = 3.14; // constant
    char grade; // char will only hold one letter. single letters must have single quotes
    char name[20]; // strings use double quotes
    //bool passing = true;
    printf("%d",num);
    printf("\nWhat is your letter grade: ");
    scanf("%c", &grade); // & is basically the same as a +=

    printf("\nTell me a number: ");
    scanf("%c", &grade);

    //this input allows you to get a space
    printf("\nWhat is your name: ");
    fgets(name, sizeof(name), stdin);
    
    printf("%d\n", num);
    printf("%s has a %c grade in this class!", name, grade);

    return 0;
}
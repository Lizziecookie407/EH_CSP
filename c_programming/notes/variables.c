// EH 6th Variables Notes
#include <stdio.h>

//What is the main difference between declaring variables in Python and C?
// must state what type of information the variable will hold - static data type
//In C, what is the purpose of specifying a data type when declaring a variable?
// saving memory. it has a specific number of bytes.
// int 4 float 4 double 8 char 1, bytes. char - list of characters for a string
//List three common data types used in C and their corresponding format specifiers for printf().
//char=c string=s digit=d float=f double=
//How do you declare and initialize an integer variable named "age" with the value 25 in C?

//What is the difference between printf() and scanf() functions in C?

//How do you add comments in C?
/*this 
will remain a comment
even on a different line
*/

//What is the purpose of the #include <stdio.h> line at the beginning of a C program?
// taking in the standard liberary input/output
//In C, what is the significance of the main() function?

//What is the difference between %d and %f format specifiers in printf()?
// %d is a place holder for a digit, one number, and %f is a place holder for a float, a number including a decimal point
//How do you print a newline character in C?
// \n
//What is the purpose of the & symbol when using scanf() to get user input?

//How do you declare a constant in C? Provide an example.
// put const in front of it

int main(void){
    int num = 4;
    const float pi = 3.14;
    char grade; // char will only hold one letter. single letters must have single quotes
    char name[20]; // strings use double quotes
    //bool passing = true;
    printf("%d",num);
    printf("\nWhat is your letter grade: ");
    scanf("%c", &grade); // & is basically the same as a +=

    printf("\nTell me a number: ");
    scanf("%c", &grade);

    //this input allows you to get a space
    fgets(name, sizeof(name), stdin);
    
    printf("%d\n", num);
    printf("%s has a %c grade in this class!", name, grade);

    return 0;
}
// EH 6th Financial Calculator

#include <stdio.h>
#include <math.h>

int main(void){

    printf("Hi, welcome to my financial calculator! Put in each amount as a plain number.");
    
    float income;
    float rent;
    float utilities;
    float groceries;
    float transportation;
    float savings = income*.1;

    (printf("Your monthly income: "));
    scanf("%f", &income);
    (printf("Your monthly rent: "));
    (printf("Your monthly utilities: "));
    (printf("Your monthly groceries: "));
    (printf("Your monthly transportation: "));

    float total_expenses = rent+utilities+groceries+transportation+savings;
    float spending = income-total_expenses;

    int percent_savings =(savings/income*100,0);
    int percent_rent = (rent/income*100, 0);
    int percent_utilities = (utilities/income*100,0);
    int percent_groceries = (groceries/income*100,0);
    int percent_transportation = (transportation/income*100,0);
    int percent_spending = (spending/income*100,0);

    printf("\nYour rent is $", rent, "and that is", percent_rent, "percent of your income.");
    printf("\nYour utilities are $", utilities, ", and that is", percent_utilities, "percent of your income.");
    printf("\nYour groceries are $", groceries, ", and that is", percent_groceries, "percent of your income.");
    printf("\nYour transportation is $", transportation, ", and that is", percent_transportation, "percent of your income.");
    printf("\nYou should save $", savings, "a month, and that is", percent_savings, "percent of your income.");
    printf("\nYou have $", spending, "of money left to spend each month, and that is",percent_spending, "percent of your income.");
    printf("\nThanks for using my calculator!");

    return 0;
}
// EH 6th Financial Calculator uhh

#include <stdio.h>
#include <math.h>

int main(void){

    printf("Hi, welcome to my financial calculator! Enter each amount as a plain number.");
    
    float income;
    float rent;
    float utilities;
    float groceries;
    float transportation;

    (printf("\nYour monthly income: "));
    scanf("%f", &income);
    (printf("Your monthly rent: "));
    scanf("%f", &rent);
    (printf("Your monthly utilities: "));
    scanf("%f", &utilities);
    (printf("Your monthly groceries: "));
    scanf("%f", &groceries);
    (printf("Your monthly transportation: "));
    scanf("%f", &transportation);

    float savings = (float)income*.1;
    float total_expenses = rent+utilities+groceries+transportation+savings;
    float spending = income-total_expenses;

    float percent_savings = (float)(savings/income*100);
    float percent_rent = (float)(rent/income*100);
    float percent_utilities = (float)(utilities/income*100);
    float percent_groceries = (float)(groceries/income*100);
    float percent_transportation = (float)(transportation/income*100);
    float percent_spending = (float)(spending/income*100);

    printf("\nYour rent is $%.2f, and that is %.0f percent of your income.",rent, percent_rent);
    printf("\nYour utilities are $ %.2f, and that is %.0f percent of your income.", utilities, percent_utilities);
    printf("\nYour groceries are $%.2f, and that is %.0f percent of your income.",groceries, percent_groceries);
    printf("\nYour transportation is $%.2f , and that is %.0f percent of your income.", transportation, percent_transportation);
    printf("\nYou should save $ %.2f a month, and that is %.0f percent of your income.", savings, percent_savings);
    printf("\nYou have $%.2f of money left to spend each month, and that is %.0f percent of your income.", spending, percent_spending);
    printf("\n\nThanks for using my calculator!");

    return 0;
}
// EH 6th Update Financial Calculator

#include <stdio.h>

int input_amount(char* amount){
    int num;
    printf("Your monthly %s: ", amount);
    scanf("%d", &num);
    return num;
}

float percent_amount(float amount, int place){
    float percent = amount/place*100;
    return percent;
}

int main(void){

    printf("Hi, welcome to my financial calculator! Enter each amount as a plain number.\n");

    float income = input_amount("income");
    float rent = input_amount("rent");
    float utilities = input_amount("utilities");
    float groceries = input_amount("groceries");
    float transportation = input_amount("transportation");
    float savings = (float)income*.1;
    float total_expenses = rent+utilities+groceries+transportation+savings;
    float spending = income-total_expenses;

    float percent_savings = percent_amount(savings, income);
    float percent_rent = percent_amount(rent,income);
    float percent_utilities = percent_amount(utilities, income);
    float percent_groceries = percent_amount(groceries, income);
    float percent_transportation = percent_amount(transportation, income);
    float percent_spending = percent_amount(spending, income);

    printf("\nYour rent is $%.2f, and that is %.0f percent of your income.",rent, percent_rent);
    printf("\nYour utilities are $ %.2f, and that is %.0f percent of your income.", utilities, percent_utilities);
    printf("\nYour groceries are $%.2f, and that is %.0f percent of your income.",groceries, percent_groceries);
    printf("\nYour transportation is $%.2f , and that is %.0f percent of your income.", transportation, percent_transportation);
    printf("\nYou should save $ %.2f a month, and that is %.0f percent of your income.", savings, percent_savings);
    printf("\nYou have $%.2f of money left to spend each month, and that is %.0f percent of your income.", spending, percent_spending);
    printf("\n\nThanks for using my calculator!");

    return 0;
}
// EH 6th Expressions Practice


#include <stdio.h>
#include <math.h>

int main(void){

    int num1 = 7-24/8*4+6;
    int num2 = 18/3-7+2*5;
    int num3 = 6*4/12+72/8-9;
    int num4 = (17-6/2)+4*3;
    int num5 = -2*(1*4-2/2)+(6+2-3);
    int num6 = -1*((3-4*7)/5)-2*24/6;
    int num7 = (3*pow(5,2)/15)-(5-pow(2,2));
    int num8 = pow(1,4)*pow(2,2)+pow(3,3)-pow(2,5)/4;
    int num9 = pow((22/2-2*5),2)+pow((4-6/6),2);

    printf("7-24/8*4+6 = %d",num1);
    printf("\n18/3-7+2*5 = %d",num2);
    printf("\n6*4/12+72/8-9 = %d",num3);
    printf("\n(17-6/2)+4* 3= %d",num4);
    printf("\n-2*(1*4-2/2)+(6+2-3) = %d",num5);
    printf("\n(-1*[(3-4*7)/5]-2*24/6) =%d",num6);
    printf("\n(3*5^2/15)-(5-2^2) = %d",num7);
    printf("\n(1^4*2^2+3^3)-2^5/4) = %d",num8);
    printf("\n(22/2-2*5)^2+(4-6/6)^2 = %d",num9);

    return 0;
}
// EH 6th Variables Practice

int main(void){
    int year = 2025; //whole numers
    float pi = 3.14; // decimals
    double long_pi; 3.14159269358979323; // decimals that are 2x as long

    printf("8/3 = %d/n", (float)8/3); //cast is specifiacally stating the data type (explicit type casting)
    printf("8/3 = %1.2f/n", 8/3.0); //only show a ceratin amount of decimals
    printf("2 ^ 4 = %f/n", pow(2,4));

    //compound assignment opperators
    year += 1;
    year ++;


    return 0;
}
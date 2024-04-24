#include <stdio.h>
#include <math.h>

int main(void) {
    double numOfHundreds, numOfFifties, numOfTwenties, numOfTens, numOfFives, numOfOnes, withdrawAmount;

    printf("Please enter the amount of money you wish to withdraw: ");
    scanf("%lf", &withdrawAmount );
        // Assuming all inputs are valid as per the given question, none of the inputs are validated. 

    numOfHundreds = trunc(withdrawAmount / 100);    // Get a whole number value for number of $100 bills
    withdrawAmount -= numOfHundreds * 100;    // To get remaining amount after giving $100 bills
    numOfFifties = trunc(withdrawAmount / 50);    // Get a whole number value for number of $50 bills
    withdrawAmount -= numOfFifties * 50;    // To get remaining amount after giving $50 bills
    numOfTwenties = trunc(withdrawAmount / 20);   // Get a whole number value for number of $20 bills
    withdrawAmount -= numOfTwenties * 20;   // To get remaining amount after giving $20 bills
    numOfTens = trunc(withdrawAmount / 10);   // Get a whole number value for number of $10 bills
    withdrawAmount -= numOfTens * 10;   // To get remaining amount after giving $10 bills
    numOfFives = trunc(withdrawAmount / 5);   // Get a whole number value for number of $5 bills
    withdrawAmount -= numOfFives * 5;   // To get remaining amount after giving $5 bills
    numOfOnes = withdrawAmount;   // Remaining amount in $1 bills

    printf("You received %0.0lf hundred(s)\n", numOfHundreds);
    printf("You received %0.0lf fifty(s)\n", numOfFifties);
    printf("You received %0.0lf twenty(s)\n", numOfTwenties);
    printf("You received %0.0lf ten(s)\n", numOfTens);
    printf("You received %0.0lf five(s)\n", numOfFives);
    printf("You received %0.0lf one(s)\n", numOfOnes);
    return 0;
}

#include <stdio.h>
#include <math.h>

int main(void) {
    double principle, annualRate, numPayments;
    
    // Getting values from the user
    printf("Please enter the amount of money you borrowed: $");
    scanf("%lf", &principle);
    printf("Please enter the annual interest rate: ");
    scanf("%lf", &annualRate);
    printf("Please enter the number of payments to be made: ");
    scanf("%lf", &numPayments);

    // For the calculation
    double interest = annualRate / 12.0;
    double monthlyPayment = (interest * principle) / (1 - (pow((1 + interest), (-numPayments))));
    double totalLoan = monthlyPayment * numPayments;
    double loanCost = totalLoan - principle;
    
    // Printing out the results
    printf("A loan of $%0.2lf with an annual interest of %0.2lf payed off over %0.0lf months will have monthly payments of $%0.2lf.\nIn total you will pay $%0.2lf, making the cost of your loan $%0.2lf.", principle, annualRate, numPayments, monthlyPayment, totalLoan, loanCost);
    return 0;
}
#include <stdio.h>
#include <math.h>

int main() {
    // Variables
    double complex1, real1, complex2, real2;
    char i, plus;
    // User input
    printf("Enter the first complex number in the form ai + b: ");
    scanf("%lf %c %c %lf", &complex1, &i, &plus, &real1);
    printf("Enter the second complex number in the form ai + b: ");
    scanf("%lf %c %c %lf", &complex2, &i, &plus, &real2);
    // Assuming all inputs are valid as per the given question, none of the inputs are validated.

    double first, last, outside, inside, imaginaryTerm, realTerm;
    // FOIL Multiplication
    first = (complex1 * complex2);
    outside = (complex1 * real2);
    inside = (complex2 * real1);
    last = (real1 * real2);
    // Putting together solution
    imaginaryTerm = outside + inside;
    realTerm = last - first;
    // Printing solution
    printf("(%0.0lfi + %0.0lf) * (%0.0lfi + %0.0lf) = %0.0lfi + %0.0lf", complex1, real1, complex2, real2, imaginaryTerm, realTerm);

    return 0;
}

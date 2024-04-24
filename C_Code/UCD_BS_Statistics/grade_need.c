#include <stdio.h>

int main(void) {
      // variables
    char letterGrade;
    double percentNeeded, percentCurrent, finalWeight;
    
      // getting values from the user
    printf("Enter the grade you want in the class: ");
    scanf("%c", &letterGrade);
    printf("Enter the percent you need to get that grade: ");
    scanf("%lf", &percentNeeded);
    printf("Enter your current percent in the class: ");
    scanf("%lf", &percentCurrent);
    printf("Enter the weight of the final: ");
    scanf("%lf", &finalWeight);


      // getting the score needed on the final
    double goalScore = ((100.0 * percentNeeded) - ((100.0 - finalWeight) * percentCurrent)) / (finalWeight);

      // printing out the necessary info.
    printf("You need to get at least %0.2lf%% on the final to get a %c in the class.", goalScore, letterGrade);
    return 0;
}
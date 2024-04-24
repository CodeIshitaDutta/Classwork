/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{
    printf("Enter first integer: ");
    int a;
    scanf("%d", &a);
    printf("Enter second integer: ");
    int b;
    scanf("%d", &b);
    printf("Enter third integer: ");
    int c;
    scanf("%d", &c);
    int e = a + b + c;
    printf("The sum is: %d", e);

    return 0;
}



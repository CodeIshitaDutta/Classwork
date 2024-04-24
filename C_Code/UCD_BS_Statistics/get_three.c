/***************
 * Write a C program that prompts the user to enter three characters, one at a time.  
 * When you ask the user for the secondand third characters, remind the user what character they last entered.  
 * The program should then print the three characters backwards.  
 * Any whitespace entered by the user should be completely ignored
 * ***********/
 
 #include <stdio.h>

int main()
{
    printf("Enter first character: ");
    char a;
    scanf(" %c", &a);
    printf("You just entered %c. Enter second character: ", a);
    char b;
    scanf(" %c", &b);
    printf("You just entered %c. Enter third character: ", b);
    char c;
    scanf(" %c", &c);
    printf("Backwards, the three characters are %c%c%c.", c, b, a);
}

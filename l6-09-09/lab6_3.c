// Code by Arjun
// Date: 09-09-2026

#include<stdio.h>
#include<string.h>

//swap function
void swap(char *a, char *b){
char temp='\0';
temp=*a;
*a=*b;
*b=temp;}

//Main program begins
int main(void){
char string[100]; //Declaring the string
printf("Enter any word: ");

fgets(string, sizeof(string), stdin); //Taking the input
string[strcspn(string, "\n")] = '\0'; // To clear \n added by fgets 

//Code for swapping
swap(&string[0], &string[1]);

//Printing modified string
printf("Modified word: %s ", string);
}

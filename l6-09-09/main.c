#include <stdio.h>


void printBorder(int count){
	for(int i=0; i<count; i++) printf("*");
	printf("\n");
}

int main(){
	int c;
	printf("Enter the nmumber of asterisks: ");
	scanf(" %d",&c);
	printBorder(c);
	printf("HI\n");
	printBorder(c);
	
}

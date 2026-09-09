//09-09-26
//code by Anvidha

#include <stdio.h>
#include <string.h>
int main()
{
	printf("Enter a string");//input a string
	char string[50];
	scanf(" %[^\n]", string);//storing
	int len;
        len=strlen(string);			 //
	printf("Enter a character in the string");
        char character;// storing the character as character
        scanf(" %c",&character);
	int found=0;
	for(int i=0; i<len;i=i+1)
	{
		if(string[i]==character)
		{
			printf("Output: %d",i);
			found=1;
			break;
		}
		
	}
	if (found==0){
                        printf("-1");}
	return 0;
}

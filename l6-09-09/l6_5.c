//09-09-26
//Code by Anvidha
#include <stdio.h>
#include <string.h>
int main()
{
	printf("Enter word");//taking input
	char word1[50];
	char word2[50];//reverse of word1
	scanf(" %[^\n]", word1);//storing
        int len;                                          len=strlen(word1);
   //making word2 reverse of word1
	for(int i = 0; i < len; i++)
        {
        word2[i] = word1[len - 1 - i];
        }
	int same=0;
    //checking whether it is palindrome or not 
        for(int j = 0; j < len; j++)
	{
	    //checking no of letters are same
	  if(word1[j]==word2[j])
	  {
		 same=same+1;
	  }
	}
	//if all are same it is palindrome
	  if(same==len)
	  {
		  printf("This is palindrome");
	  }
	  else
	  {
	      printf("This is not palindrome");
	  }
	
return 0;
}
	

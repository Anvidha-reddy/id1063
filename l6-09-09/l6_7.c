//09-09-26
//code by Anvidha

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n; 
    char *str;
    char x, y;
// taking input of length
    printf("Enter length of word: ");
    scanf("%d", &n);

    str = (char *)malloc((n + 1) * sizeof(char));
//taking input of word
    printf("Enter word: ");
    scanf("%s", str);
//the letter to be replaced 
    printf("Enter x: ");
    scanf(" %c", &x);
// the letter to replace
    printf("Enter y: ");
    scanf(" %c", &y);
//loop to replace
    for (int i = 0; i<n ; i++)
    {
        if (str[i] == x)
            str[i] = y;
    }
// printing the new word
    printf("Modified word: %s\n", str);

    free(str);

    return 0;
}

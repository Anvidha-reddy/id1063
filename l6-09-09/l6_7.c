//09-09-26
//code by Anvidha

#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    char *str;
    char x, y;

    printf("Enter length of word: ");
    scanf("%d", &n);

    str = (char *)malloc((n + 1) * sizeof(char));

    printf("Enter word: ");
    scanf("%s", str);

    printf("Enter x: ");
    scanf(" %c", &x);

    printf("Enter y: ");
    scanf(" %c", &y);

    for (int i = 0; str[i] != '\0'; i++)
    {
        if (str[i] == x)
            str[i] = y;
    }

    printf("Modified word: %s\n", str);

    free(str);

    return 0;
}

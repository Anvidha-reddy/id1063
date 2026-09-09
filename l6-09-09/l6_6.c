#include <stdio.h>
#include <stdlib.h>

int main()
{
    int n;
    char *str;

    printf("Enter n: ");
    scanf("%d", &n);
// taken from cprog codes matfun.h line 99
    str = (char *)malloc((n + 1) * sizeof(char));

    printf("Enter %d characters: ", n);

    for (int i = 0; i < n; i++)
    {
        scanf(" %c", &str[i]);
    }

    str[n] = '\0';

    printf("String: %s\n", str);

    

    return 0;
}

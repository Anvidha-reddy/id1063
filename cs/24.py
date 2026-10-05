#include <stdio.h>

int main()
{
    int a, b, c, X;

    printf("a b c | X\n");
    printf("--------------\n");

    for (a = 0; a <= 1; a++)
    {
        for (b = 0; b <= 1; b++)
        {
            for (c = 0; c <= 1; c++)
            {
                X = (a && b) || (a && c) || (b && c);

                printf("%d %d %d | %d\n", a, b, c, X);
            }
        }
    }

    return 0;
}

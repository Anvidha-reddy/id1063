#include <stdio.h>

int main()
{
    int kmap[2][4] = {
        {0, 0, 1, 0},
        {0, 1, 1, 1}
    };

    int a, b, c, col, X;

    /* ---------- K-MAP ---------- */

    printf("K-MAP\n\n");
    printf("       00  01  11  10\n");
    printf("a=0    %d   %d   %d   %d\n",
           kmap[0][0], kmap[0][1], kmap[0][2], kmap[0][3]);

    printf("a=1    %d   %d   %d   %d\n",
           kmap[1][0], kmap[1][1], kmap[1][2], kmap[1][3]);

    /* ---------- K-MAP GROUPS ---------- */

    printf("\nK-map groups:\n");

    printf("m3, m7 -> bc\n");
    printf("m5, m7 -> ac\n");
    printf("m6, m7 -> ab\n");

    printf("\nExpression obtained using K-map:\n");
    printf("X = ab + ac + bc\n");

    /* ---------- TRUTH TABLE ---------- */

    printf("\nTRUTH TABLE\n");
    printf("a b c | X\n");
    printf("--------------\n");

    for (a = 0; a <= 1; a++)
    {
        for (b = 0; b <= 1; b++)
        {
            for (c = 0; c <= 1; c++)
            {
                /* Find corresponding K-map column */
                if (b == 0 && c == 0)
                    col = 0;
                else if (b == 0 && c == 1)
                    col = 1;
                else if (b == 1 && c == 1)
                    col = 2;
                else
                    col = 3;

                /* Get output from K-map */
                X = kmap[a][col];

                printf("%d %d %d | %d\n", a, b, c, X);
            }
        }
    }

    return 0;
}

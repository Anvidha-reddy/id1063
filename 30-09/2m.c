//Code by Mudit
//Date: 30/09/2026
#include <stdio.h>
#include <stdlib.h>
#include "coeffs.h"

void binaryVector(int n)
{
    double x;

    // Generate n random numbers using uniform() function
    uniform("binary.dat", n);

    FILE *fp = fopen("binary.dat", "r");

    // Convert the random numbers into 0 or 1
    for (int i = 0; i < n; i++)
    {
        fscanf(fp, "%lf", &x);

        if (x < 0.5)
            printf("0 ");
        else
            printf("1 ");
    }

    printf("\n");
    fclose(fp);
}

int main()
{
    int n;

    // Read the length of the binary vector
    printf("Enter n: ");
    scanf("%d", &n);

    binaryVector(n);

    return 0;
}

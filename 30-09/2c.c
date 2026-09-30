#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void uniform(char *str, int len) {
    int i;
    FILE *fp;
    fp = fopen(str, "w");
    // Generate numbers
    for (i = 0; i < len; i++) {
        fprintf(fp, "%lf\n", (double)rand() / RAND_MAX);
    }
    fclose(fp);
}

void binaryMatrix(int n, int m) {
    double x;
    int total = n * m;

    // Generate n * m random numbers using uniform() function
    uniform("binary.dat", total);

    FILE *fp = fopen("binary.dat", "r");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return;
    }

    printf("\nGenerated %dx%d Binary Matrix:\n", n, m);

    // Read uniform values and print in matrix rows and columns
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            fscanf(fp, "%lf", &x);

            if (x < 0.5)
                printf("0 ");
            else
                printf("1 ");
        }
        printf("\n"); // Move to next row
    }

    fclose(fp);
}

int main(void) {
    srand(time(NULL));

    int n, m;
    printf("Enter number of rows (n): ");
    scanf("%d", &n);

    printf("Enter number of columns (m): ");
    scanf("%d", &m);

    binaryMatrix(n, m);

    return 0;
}


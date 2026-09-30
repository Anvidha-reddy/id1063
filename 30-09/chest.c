#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void uniform(char *str, int len) {
    int i;
    FILE *fp;
    fp = fopen(str, "w");
    for (i = 0; i < len; i++) {
        fprintf(fp, "%lf\n", (double)rand() / RAND_MAX);
    }
    fclose(fp);
}

int main(void) {
    // Seed random number generator with system time
    srand(time(NULL));

    int n;
    printf("Enter number of entries (n): ");
    if (scanf("%d", &n) != 1 || n <= 0) {
        printf("Invalid input.\n");
        return 1;
    }

    // 1. Generate n random values into uniform dat file
    uniform("chests.dat", n);

    FILE *fp = fopen("chests.dat", "r");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    int coins[n];
    double x;

    // 2. Read values and scale double [0, 1) to integer coins [1, 100]
    for (int i = 0; i < n; i++) {
        fscanf(fp, "%lf", &x);
        coins[i] = 1 + (int)(x * 100);
        if (coins[i] > 100) coins[i] = 100;
    }
    fclose(fp);

    // 3. Print the randomly generated initial chest array
    printf("\nRandomly Generated Array:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", coins[i]);
    }
    printf("\n");

    // 4. Use a pointer to find the chest with the minimum coins
    int *min_ptr = &coins[0];
    for (int i = 1; i < n; i++) {
        if (coins[i] < *min_ptr) {
            min_ptr = &coins[i];
        }
    }

    // 5. Remove coins from the cursed chest
    *min_ptr = 0;

    // 6. Print the modified array
    printf("\nModified Array (Cursed chest set to 0):\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", coins[i]);
    }
    printf("\n");

    return 0;
}


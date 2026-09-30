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

void sampleVector(int n) {
    double x;

    // Generate n random numbers in uniform file
    uniform("samples.dat", n);

    FILE *fp = fopen("samples.dat", "r");
    if (fp == NULL) {
        printf("Error opening file.\n");
        return;
    }

    printf("Samples (1 to 100):\n[ ");
    for (int i = 0; i < n; i++) {
        fscanf(fp, "%lf", &x);

        // Map x in [0, 1) to integer in range [1, 100]
        int sample = 1 + (int)(x * 100);
        
        // Edge case handling if x == 1.0
        if (sample > 100) sample = 100;

        printf("%d ", sample);
    }
    printf("]\n");

    fclose(fp);
}

int main(void) {
    srand(time(NULL));

    int n;
    printf("Enter number of samples (n): ");
    scanf("%d", &n);

    sampleVector(n);

    return 0;
}


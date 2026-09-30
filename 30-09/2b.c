#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include "coeffs.h"

// Define function ABOVE main() so C recognizes it
void print_binary_vector(int n) {
    uniform("uni.dat", n);

    FILE *fp = fopen("uni.dat", "r");
    if (fp == NULL) {
        printf("Error opening uni.dat\n");
        return;
    }

    double u;
    printf("[ ");
    for (int i = 0; i < n; i++) {
        if (fscanf(fp, "%lf", &u) == 1) {
            int bit = (u >= 0.5) ? 1 : 0;
            printf("%d ", bit);
        }
    }
    printf("]\n");

    fclose(fp);
}

int main(void) {
    int n = 10;
    print_binary_vector(n);
    return 0;
}


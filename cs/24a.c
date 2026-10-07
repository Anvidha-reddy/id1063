// Code by Anvidha
// Date: 05/10/2026
#include <stdio.h>

// Helper function to fill A, B, and C directly from an integer
void int_to_3bits(int num, int *a, int *b, int *c) {
    *a = (num >> 2) & 1;
    *b = (num >> 1) & 1;
    *c = num & 1;
}

int main()
{
    int i, A, B, C, X;

    printf("A B C | X\n");
    printf("--------\n");

    for (i = 0; i < 8; i++)
    {
        // Set A, B, C in a single function call
        int_to_3bits(i, &A, &B, &C);

        // Majority function: X = AB + AC + BC
        X = (A & B) | (A & C) | (B & C);

        printf("%d %d %d | %d\n", A, B, C, X);
    }

    return 0;
}


// Code by Anvidha
// Date: 05/10/2026
#include <stdio.h>

// Function to print a number directly as binary
void print_binary(int num, int bits) {
    for (int i = bits - 1; i >= 0; i--) {
        // Shift right by 'i' positions and extract the last bit using & 1
        printf("%d ", (num >> i) & 1);
    }
}

int main() {
    int bits = 3;            // Set total bits required (e.g., 3 for 8 combinations)
    int total = 1 << bits;   // Calculates 2^3 = 8

    printf("Binary | X\n");
    printf("-------\n");

    for (int i = 0; i < total; i++) {
        // 1. Directly print binary of integer 'i'
        print_binary(i, bits);

        // 2. Compute majority function using direct bit extractions from 'i'
        // Bit 2 = A, Bit 1 = B, Bit 0 = C
        int A = (i >> 2) & 1;
        int B = (i >> 1) & 1;
        int C = i & 1;
        int X = (A & B) | (A & C) | (B & C);

        // 3. Print output
        printf("| %d\n", X);
    }

    return 0;
}


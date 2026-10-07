#include <stdio.h>

// Function that extracts bits of 'num' into an array
void int_to_binary_array(int num, int bits[], int size) {
    for (int i = 0; i < size; i++) {
        bits[size - 1 - i] = (num >> i) & 1;
    }
}

// Majority function X(a, b, c): output 1 if at least two inputs are 1
int X(int a, int b, int c) {
    return (a && b) || (b && c) || (c && a);
}

int main() {
    // Flags to check if statements hold for ALL combinations
    int optA_correct = 1;
    int optB_correct = 1;
    int optC_correct = 1;
    int optD_correct = 1;

    // Loop through all 2^5 = 32 combinations of (a, b, c, d, e)
    for (int i = 0; i < 32; i++) {
        int vars[5]; // vars[0]=a, vars[1]=b, vars[2]=c, vars[3]=d, vars[4]=e
        int_to_binary_array(i, vars, 5);

        int a = vars[0], b = vars[1], c = vars[2], d = vars[3], e = vars[4];

        // Option A: X(a, b, X(c, d, e)) == X(X(a, b, c), d, e)
        if (X(a, b, X(c, d, e)) != X(X(a, b, c), d, e)) {
            optA_correct = 0;
        }

        // Option B: X(a, b, X(a, b, c)) == X(a, b, c)
        if (X(a, b, X(a, b, c)) != X(a, b, c)) {
            optB_correct = 0;
        }

        // Option C: X(a, b, X(a, c, d)) == (X(a, b, a) && X(c, d, c))
        if (X(a, b, X(a, c, d)) != (X(a, b, a) && X(c, d, c))) {
            optC_correct = 0;
        }

        // Option D: X(a, b, c) == X(a, X(a, b, c), X(a, c, c))
        if (X(a, b, c) != X(a, X(a, b, c), X(a, c, c))) {
            optD_correct = 0;
        }
    }

    // Output Verification Results
    printf("=== GATE Question Verification Results ===\n");
    printf("Option A: %s\n", optA_correct ? "CORRECT" : "INCORRECT");
    printf("Option B: %s\n", optB_correct ? "CORRECT" : "INCORRECT");
    printf("Option C: %s\n", optC_correct ? "CORRECT" : "INCORRECT");
    printf("Option D: %s\n", optD_correct ? "CORRECT" : "INCORRECT");

    return 0;
}


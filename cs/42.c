#include <stdio.h>

int main() {
    printf("Evaluating F = (~b1 & ~b0) | (~b2 & ~b0) | (b3 & ~b2 & b1)\n\n");
    printf("-----------------------------------------\n");
    printf(" Minterm | b3  b2  b1  b0 | Target | Equation \n");
    printf("-----------------------------------------\n");

    for (int m = 0; m < 16; m++) {
        // Extract 1-bit binary values directly using bitwise AND and shift
        int b0 = (m >> 0) & 1;
        int b1 = (m >> 1) & 1;
        int b2 = (m >> 2) & 1;
        int b3 = (m >> 3) & 1;

        // Target function: m in {0, 2, 4, 8, 10, 11, 12}
        int target = (m == 0 || m == 2 || m == 4 || m == 8 || m == 10 || m == 11 || m == 12);

        // Minimized SOP Expression using Bitwise Operators
        // ~ (NOT), & (AND), | (OR), bitwise masked with & 1 to ensure 1-bit boolean results
        int term1 = (~b1 & 1) & (~b0 & 1);          // b1' * b0'
        int term2 = (~b2 & 1) & (~b0 & 1);          // b2' * b0'
        int term3 = b3 & (~b2 & 1) & b1;            // b3 * b2' * b1

        int equation = term1 | term2 | term3;

        printf("   m%-2d   |  %d   %d   %d   %d  |   %d    |    %d\n", 
               m, b3, b2, b1, b0, target, equation);
    }

    printf("-----------------------------------------\n");

    return 0;
}


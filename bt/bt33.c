//10-09-26
//Code by Anvidha

#include <stdio.h>
#include <math.h>

// Function to calculate the next iteration (x_n+1) using Newton-Raphson
double next_iteration(double x_n) {
    return x_n - 1.0 + 2.0 * exp(-x_n);
}

int main() {
    double x0 = 1.0;// given in question
    double x1 = next_iteration(x0);

    printf("Initial guess (x0): %.6f\n", x0);
    printf("Next iteration (x1): %.6f\n", x1);

    return 0;
}


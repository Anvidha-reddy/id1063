#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function from the question that counts swaps
int fun(int A[], int n) {
    int swap_count = 0;
    for (int i = 0; i <= n - 2; i++) {
        for (int j = 0; j <= n - i - 2; j++) {
            if (A[j] > A[j + 1]) {
                // Swap A[j] and A[j+1]
                int temp = A[j];
                A[j] = A[j + 1];
                A[j + 1] = temp;
                
                swap_count++;
            }
        }
    }
    return swap_count;
}

// Helper function to generate an array with values from uniform distribution [0, max_val]
void generate_uniform_array(int A[], int n, int max_val) {
    for (int i = 0; i < n; i++) {
        // Uniform distribution between 0 and max_val inclusive
        A[i] = rand() % (max_val + 1);
    }
}

int main() {
    int n = 30;
    int max_val = 100;
    int A[30];

    // Initialize random number generator seed
    srand(time(NULL));

    // 1. Generate array A from uniform distribution
    generate_uniform_array(A, n, max_val);

    printf("Generated Uniform Array A[0...29]:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", A[i]);
    }
    printf("\n\n");

    // 2. Count swaps using fun() for this random uniform array
    int random_swaps = fun(A, n);
    printf("Swaps required for this random uniform array: %d\n", random_swaps);


    return 0;
}


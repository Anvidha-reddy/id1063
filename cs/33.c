#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Function from pseudocode that sorts array and counts total swaps
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

int main() {
    int n = 30;
    int max_val = 100;
    int A[30];

    // Initialize random seed based on current time
    srand(time(NULL));

    // Generate array A from uniform distribution [0, 100]
    for (int i = 0; i < n; i++) {
        A[i] = rand() % (max_val + 1);
    }

    // Print Original Array
    printf("Original Array A[0...29]:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", A[i]);
    }
    printf("\n\n");

    // Run fun() to sort and get total swaps
    int total_swaps = fun(A, n);

    // Print Output (Sorted) Array
    printf("Output Array (Sorted) A[0...29]:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", A[i]);
    }
    printf("\n\n");

    // Print Swaps
    printf("Total swap operations performed: %d\n", total_swaps);

    return 0;
}



#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n;
    
    // Read total number of treasure chests
    if (scanf("%d", &n) != 1 || n <= 0) {
        return 0;
    }

    int coins[n];

    // Read the number of coins in each chest
    for (int i = 0; i < n; i++) {
        scanf("%d", &coins[i]);
    }

    // Pointer to keep track of the chest with the fewest coins
    int *min_ptr = &coins[0];

    // Scan array using pointer logic to find the minimum element
    for (int i = 1; i < n; i++) {
        if (coins[i] < *min_ptr) {
            min_ptr = &coins[i]; // Update pointer to point to the new minimum
        }
    }

    // Remove all coins from the cursed chest by setting its value to 0
    *min_ptr = 0;

    // Print the updated array
    for (int i = 0; i < n; i++) {
        printf("%d", coins[i]);
        if (i < n - 1) {
            printf(" ");
        }
    }
    printf("\n");

    return 0;
}


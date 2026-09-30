#include <stdio.h>


int productEntry(int A[][MAX], int B[][MAX], int row, int col, int common) {
    int sum = 0;
    for (int k = 0; k < common; k++) {
        sum += A[row][k] * B[k][col];
    }
    return sum;
}

int main() {
    int r1, c1, r2, c2;
    int A[MAX][MAX], B[MAX][MAX];

    // Read Matrix A dimensions and elements
    scanf("%d %d", &r1, &c1);
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c1; j++) {
            scanf("%d", &A[i][j]);
        }
    }

    // Read Matrix B dimensions and elements
    scanf("%d %d", &r2, &c2);
    for (int i = 0; i < r2; i++) {
        for (int j = 0; j < c2; j++) {
            scanf("%d", &B[i][j]);
        }
    }

    // Print product matrix
    for (int i = 0; i < r1; i++) {
        for (int j = 0; j < c2; j++) {
            printf("%d ", productEntry(A, B, i, j, c1));
        }
        printf("\n");
    }

    return 0;
}


#include <stdio.h>

int firstStable(double a[], int n, double tolerance) {
    for (int i = 0; i < n - 1; i++) {
        double diff = a[i+1] - a[i];
        if (diff < 0) {
            diff = -diff; //absolute value
        }

        if (diff <= tolerance+1e-9) {
            return i; // satisfies condition
        }
    }
    return -1;
}

int main() {
    int n;
    double tolerance;

    printf("Enter n: ");
    if (scanf("%d", &n) != 1 || n < 2) {
        return 1;
    }

    double a[n];
    printf("Enter the readings: ");
    for (int i = 0; i < n; i++) {
        scanf("%lf", &a[i]);
    }

    printf("Enter tolerance: ");
    scanf("%lf", &tolerance);

    printf("%d\n", firstStable(a, n, tolerance));

    return 0;
}


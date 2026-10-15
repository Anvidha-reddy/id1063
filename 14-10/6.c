#include <stdio.h>

struct Polynomial {i
    int degree;       // Degree n (up to 20)
    double coeff[21]; //Array to store a0, a1., an
};

// Function to evaluate P(x) using Horner's Method
double evaluate(struct Polynomial poly, double x) {
    double result = poly.coeff[poly.degree]; // Start with the highest degree coefficient (an)

    // Loop downwards from an-1 down to a0
    for (int i = poly.degree - 1; i >= 0; i--) {
        result = result * x + poly.coeff[i];
    }

    return result;
}

// Function to compute the derivative of a polynomial
struct Polynomial compute_derivative(struct Polynomial poly) {
    struct Polynomial deriv;

    // If degree is 0 (constant term), derivative is 0
    if (poly.degree == 0) {
        deriv.degree = 0;
        deriv.coeff[0] = 0;
        return deriv;
    }

    // Derivative degree is (n - 1)
    deriv.degree = poly.degree - 1;

    // d/dx (a_i * x^i) = i * a_i * x^(i-1)
    for (int i = 1; i <= poly.degree; i++) {
        deriv.coeff[i - 1] = i * poly.coeff[i];
    }

    return deriv;
}

int main() {
    struct Polynomial p;
    double a;

    printf("Enter degree of polynomial n (<= 20): ");
    scanf("%d", &p.degree);

    printf("Enter coefficients from a0 to a%d:\n", p.degree);
    for (int i = 0; i <= p.degree; i++) {
        printf("a%d: ", i);
        scanf("%lf", &p.coeff[i]);
    }

    printf("Enter evaluation point a: ");
    scanf("%lf", &a);

    // (i) Evaluate P(a)
    double val = evaluate(p, a);
    printf("\nValue of P(%.2f) = %.2f\n", a, val);

    // (ii) Compute Derivative
    struct Polynomial dp = compute_derivative(p);

    printf("\nDerivative Polynomial (Degree %d):\n", dp.degree);
    for (int i = 0; i <= dp.degree; i++) {
        printf("Coeff of x^%d = %.2f\n", i, dp.coeff[i]);
    }

    return 0;
}


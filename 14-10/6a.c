//Code by anvidha
//14-10-26
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Node structure for linked list
typedef struct Node {
    double coeff;
    struct Node* next;
} Node;

// Helper function to create a new node
Node* createNode(double coeff) {
    Node* newNode = (Node*)malloc(sizeof(Node));
    newNode->coeff = coeff;
    newNode->next = NULL;
    return newNode;
}

// Helper function to append a node to the list
void append(Node** head, double coeff) {
    Node* newNode = createNode(coeff);
    if (*head == NULL) {
        *head = newNode;
        return;
    }
    Node* temp = *head;
    while (temp->next != NULL) {
        temp = temp->next;
    }
    temp->next = newNode;
}

int main() {
    Node* poly = NULL;
    char buffer[256];

    printf("Enter coefficients (a0 a1 a2 ...) separated by spaces, then press ENTER:\n");
    
    // Read the entire line until Enter is pressed
    if (fgets(buffer, sizeof(buffer), stdin) != NULL) {
        char* token = strtok(buffer, " \t\n");
        while (token != NULL) {
            double c = atof(token); // Convert text token to double
            append(&poly, c);
            token = strtok(NULL, " \t\n");
        }
    }

    if (poly == NULL) {
        printf("Error: No coefficients entered.\n");
        return 1;
    }

    // Accept floating-point number
    double a;
    printf("\nEnter the floating-point number a: ");
    scanf("%lf", &a);

    // (i) Compute and print the value of P(a) using the list
    double p_val = 0.0;
    double x_power = 1.0;
    Node* curr = poly;

    while (curr != NULL) {
        p_val += curr->coeff * x_power;
        x_power *= a;
        curr = curr->next;
    }
    printf("\n(i) Value of P(%.2f) = %.4f\n", a, p_val);

    // (ii) Compute the derivative and store it in another linked list
    Node* deriv = NULL;
    
    if (poly->next == NULL) {
        append(&deriv, 0.0);
    } else {
        curr = poly->next; // Skip constant term a0
        int power = 1;
        while (curr != NULL) {
            double d_coeff = power * curr->coeff; // d/dx(a_k * x^k) = k * a_k
            append(&deriv, d_coeff);
            power++;
            curr = curr->next;
        }
    }

    return 0;
}


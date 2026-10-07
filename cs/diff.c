#include <stdio.h>



int main() {
    int a = 12; // Binary: 1100
    int b = 25; // Binary: 11001
    printf("a=%d\n",a);
    printf("b=%d\n",b);
    printf("=== 1. OUTPUT DIFFERENCE ===\n");
    printf("a & b  = %d\n", a & b);   // Bitwise result
    printf("a && b = %d\n\n", a && b); // Logical result

    return 0;
}


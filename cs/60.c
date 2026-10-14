//Code by Anvidha
//12-10-26
#include <stdio.h>

int main() {
    // Initial state: Q0 Q1 Q2 Q3 = 0 0 0 0
    int Q0 = 0, Q1 = 0, Q2 = 0, Q3 = 0;
    
    // Store initial state to detect when the cycle completes
    int init_Q0 = Q0, init_Q1 = Q1, init_Q2 = Q2, init_Q3 = Q3;
    
    int clock_step = 0;

    printf("====================================================\n");
    printf(" Clock Step |  Q0  Q1  Q2  Q3  | Next State Inputs  \n");
    printf("            | (Present State) | D0  D1  D2  D3     \n");
    printf("====================================================\n");

    do {
        // Circuit flip-flop input logic:
        // D0 = ~Q3, D1 = Q0, D2 = Q1, D3 = Q2
        int D0 = !Q3;
        int D1 = Q0;
        int D2 = Q1;
        int D3 = Q2;

        printf("     %2d     |   %d   %d   %d   %d   |  %d   %d   %d   %d\n", 
               clock_step, Q0, Q1, Q2, Q3, D0, D1, D2, D3);

  // State transition on Clock Edge: Q_next = D
        Q0 = D0;
        Q1 = D1;
        Q2 = D2;
        Q3 = D3;

        clock_step++;

    } while (!(Q0 == init_Q0 && Q1 == init_Q1 && Q2 == init_Q2 && Q3 == init_Q3));

    // Print final state returning to initial
    printf("     %2d     |   %d   %d   %d   %d   |  (Returned to Initial)\n", 
           clock_step, Q0, Q1, Q2, Q3);
    printf("====================================================\n");
    printf("Total distinct states traversed before returning: %d\n", clock_step);

    return 0;
}


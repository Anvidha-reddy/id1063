iinclude <math.h>
#include <stdlib.h>
#include "libs/listgen.h"
#include "libs/listfun.h"

int main(void){
    avvyuh *A, *B;

    A = loadList("a.dat", 1, 9);
    B = loadList("b.dat", 1, 7);

    printList(A);
    printList(B);

    return 0;
}

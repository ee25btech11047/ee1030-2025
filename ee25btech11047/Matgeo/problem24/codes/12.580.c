#include <stdio.h>

int main() {
    int n = 3; // 3x3 matrix
    int complex_entries = n * n;  // total complex entries
    
    // Step 1: Dimension of V (all complex entries over R)
    int dimV = complex_entries * 2; // 2 real numbers per complex entry

    // Step 2: Dimension of W1 (Hermitian)
    // Diagonal entries: n real numbers
    // Off-diagonal entries: n*(n-1)/2 complex numbers = (n*(n-1)) real
    int dimW1 = n + (n*(n-1)); // 3 + 6 = 9

    // Step 3: Dimension of W2 (trace zero)
    // Trace=0 gives 1 complex constraint = 2 real
    int dimW2 = dimV - 2; // 18 - 2 = 16

    // Step 4: Dimension of W1 ∩ W2
    int dimIntersection = dimW1 - 1; // 1 real reduction from trace constraint

    // Step 5: Dimension of W1 + W2
    int dimSum = dimW1 + dimW2 - dimIntersection;

    printf("%d\n", dimSum);

    return 0;
}

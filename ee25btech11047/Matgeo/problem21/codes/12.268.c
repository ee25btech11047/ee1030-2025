#include <stdio.h>

int main() {
    int trace = 11;
    int det = 36;
    int i, j, k;

    printf("The positive integer eigenvalues are:\n");

    for(i = 1; i <= trace; i++) {           // possible first eigenvalue
        for(j = 1; j <= trace - i; j++) {   // second eigenvalue
            k = trace - i - j;              // third eigenvalue from trace
            if(k > 0 && i * j * k == det) { // check product = determinant
                printf("Eigenvalues: %d, %d, %d\n", i, j, k);
                int max = i;
                if(j > max) max = j;
                if(k > max) max = k;
                printf("Largest eigenvalue: %d\n", max);
            }
        }
    }

    return 0;
}

#include <stdio.h>

int find_largest_eigen(int trace, int det) {
    int i, j, k, max = 0;

    for(i = 1; i <= trace; i++) {
        for(j = 1; j <= trace - i; j++) {
            k = trace - i - j;
            if(k > 0 && i * j * k == det) {
                // Find the largest eigenvalue
                max = i;
                if(j > max) max = j;
                if(k > max) max = k;
            }
        }
    }
    return max;
}

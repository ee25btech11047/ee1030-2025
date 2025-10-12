#include <stdio.h>

long compute_result() {
    int A[3][3] = {
        {3, -1, 1},
        {-1, 5, -1},
        {1, -1, 3}
    };

    long trace = A[0][0] + A[1][1] + A[2][2];

    // Determinant computed manually (safe for ctypes)
    long det = A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
             - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
             + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]);

    return det * trace;
}

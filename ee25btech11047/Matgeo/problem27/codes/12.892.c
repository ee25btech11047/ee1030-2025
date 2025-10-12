#include <stdio.h>

int main() {
    int A[3][3] = {
        {3, -1, 1},
        {-1, 5, -1},
        {1, -1, 3}
    };

    int trace = 0;
    for (int i = 0; i < 3; i++) {
        trace += A[i][i];
    }

    // Compute determinant using cofactor expansion along first row
             int det = A[0][0]*(A[1][1]*A[2][2] - A[1][2]*A[2][1])
             - A[0][1]*(A[1][0]*A[2][2] - A[1][2]*A[2][0])
             + A[0][2]*(A[1][0]*A[2][1] - A[1][1]*A[2][0]);


    int result = det * trace;

    printf("Trace = %d\n", trace);
    printf("Determinant = %d\n", det);
    printf("lambda1*lambda2*lambda3*(lambda1+lambda2+lambda3) = %d\n", result);

    return 0;
}

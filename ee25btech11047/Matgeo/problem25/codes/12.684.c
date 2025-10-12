 #include <stdio.h>
#include <math.h>

#define N 3  // Dimension of the square matrix
#define EPS 1e-6  // Tolerance for floating-point comparison

int main() {
    int i, j, k;
    double A[N][N] = {
        {1/sqrt(2), -1/sqrt(2), 0},
        {1/sqrt(2),  1/sqrt(2), 0},
        {0,          0,         1}
    };
    double AA_T[N][N] = {0};

    // Compute AA^T
    for(i = 0; i < N; i++) {
        for(j = 0; j < N; j++) {
            for(k = 0; k < N; k++) {
                AA_T[i][j] += A[i][k] * A[j][k];  // Note: A^T is used by swapping indices
            }
        }
    }

    // Check if AA^T is identity
    int isOrthogonal = 1;
    for(i = 0; i < N; i++) {
        for(j = 0; j < N; j++) {
            if(i == j && fabs(AA_T[i][j] - 1) > EPS) isOrthogonal = 0;
            if(i != j && fabs(AA_T[i][j]) > EPS) isOrthogonal = 0;
        }
    }

    printf("Matrix A is orthogonal? %d\n", isOrthogonal); // 1=true, 0=false

    return 0;
}

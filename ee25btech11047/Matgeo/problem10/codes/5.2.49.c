#include <stdio.h>
#include <math.h>

#define N 3

int main() {
    int i, j, k;
    double A[N][N+1] = {
        {3, -1, -2, 2},
        {0,  2, -1, -1},
        {3, -5,  0, 3}
    };

    // Forward elimination
    for (i = 0; i < N; i++) {
        // Pivot should not be zero (no pivoting added here for simplicity)
        if (fabs(A[i][i]) < 1e-9) continue;

        // Normalize row
        double div = A[i][i];
        for (j = i; j <= N; j++) {
            A[i][j] /= div;
        }

        // Eliminate other rows
        for (k = 0; k < N; k++) {
            if (k == i) continue;
            double factor = A[k][i];
            for (j = i; j <= N; j++) {
                A[k][j] -= factor * A[i][j];
            }
        }
    }

    // Check for inconsistency
    int inconsistent = 0;
    for (i = 0; i < N; i++) {
        int allZero = 1;
        for (j = 0; j < N; j++) {
            if (fabs(A[i][j]) > 1e-9) {
                allZero = 0;
                break;
            }
        }
        if (allZero && fabs(A[i][N]) > 1e-9) {
            inconsistent = 1;
            break;
        }
    }

    if (inconsistent) {
        printf("System is inconsistent -> No solution\\n");
    } else {
        printf("Solution:\\n");
        for (i = 0; i < N; i++) {
            printf("x%d = %lf\\n", i+1, A[i][N]);
        }
    }

    return 0;
}


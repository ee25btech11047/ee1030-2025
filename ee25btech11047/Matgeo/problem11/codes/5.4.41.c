#include <stdio.h>

int main() {
    int i, j, k;
    double A[3][3] = {
        {2, 1, 3},
        {4, -1, 0},
        {-7, 2, 1}
    };

    double I[3][3] = {
        {1, 0, 0},
        {0, 1, 0},
        {0, 0, 1}
    };

    // Perform Gauss-Jordan elimination
    for (i = 0; i < 3; i++) {
        // Make the diagonal element 1
        double diag = A[i][i];
        for (j = 0; j < 3; j++) {
            A[i][j] /= diag;
            I[i][j] /= diag;
        }

        // Make other elements in the column 0
        for (k = 0; k < 3; k++) {
            if (k != i) {
                double factor = A[k][i];
                for (j = 0; j < 3; j++) {
                    A[k][j] -= factor * A[i][j];
                    I[k][j] -= factor * I[i][j];
                }
            }
        }
    }

    // Print the inverse
    printf("Inverse matrix is:\n");
    for (i = 0; i < 3; i++) {
        for (j = 0; j < 3; j++) {
            printf("%8.3f ", I[i][j]);
        }
        printf("\n");
    }

    return 0;
}


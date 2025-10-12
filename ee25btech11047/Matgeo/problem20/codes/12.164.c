#include <stdio.h>
#include <math.h>

int main() {
    // Matrix A
    double A[3][3] = {
        {1, 1, 1},
        {0, 1, 1},
        {0, 0, 1}
    };

    // Step 1: Since A is upper triangular, eigenvalues are diagonal elements
    double lambda[3];
    for (int i = 0; i < 3; i++) {
        lambda[i] = A[i][i];
    }

    printf("Eigenvalues:\n");
    for (int i = 0; i < 3; i++) {
        printf("λ%d = %.2f\n", i+1, lambda[i]);
    }

    // Step 2: All eigenvalues are equal (1), find eigenvectors for λ = 1
    // (A - I)
    double AI[3][3];
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            AI[i][j] = A[i][j];
            if (i == j) AI[i][j] -= 1.0;
        }
    }

    printf("\nMatrix (A - I):\n");
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 3; j++) {
            printf("%6.2f ", AI[i][j]);
        }
        printf("\n");
    }

    // From manual solving:
    // x3 = 0, x2 = 0, x1 = free → 1 eigenvector
    printf("\nEigenvector corresponding to λ = 1:\n");
    printf("v1 = [1 0 0]^T\n");

    printf("\nMaximum number of linearly independent eigenvectors = 1\n");
    return 0;
}


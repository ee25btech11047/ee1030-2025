#include <stdio.h>

int main(void) {
    // Basis matrix U: columns are u1,u2,u3 but stored row-major U[row][col]
    double U[3][3] = {
        {1.0, 1.0, 1.0},
        {0.0, 1.0, 1.0},
        {0.0, 0.0, 1.0}
    };

    // f as row vector (f = (1,1,1))
    double f[3] = {1.0, 1.0, 1.0};

    // alpha will store the row vector alpha = f * U
    double alpha[3] = {0.0, 0.0, 0.0};

    // Compute alpha_j = sum_k f_k * U[k][j]
    for (int j = 0; j < 3; ++j) {
        double sum = 0.0;
        for (int k = 0; k < 3; ++k) {
            sum += f[k] * U[k][j];
        }
        alpha[j] = sum;
    }

    // Print result
    printf("alpha = (");
    for (int j = 0; j < 3; ++j) {
        printf("%.0f", alpha[j]);            // integer values expected, print without decimals
        if (j < 2) printf(", ");
    }
    printf(")\n");

    return 0;
}

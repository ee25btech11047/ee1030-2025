#include <stdio.h>

void compute_alpha(double U[3][3], double f[3], double alpha[3]) {
    for (int j = 0; j < 3; ++j) {
        double sum = 0.0;
        for (int k = 0; k < 3; ++k) {
            sum += f[k] * U[k][j];
        }
        alpha[j] = sum;
    }
}

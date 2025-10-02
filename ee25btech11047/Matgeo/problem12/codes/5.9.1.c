#include <stdio.h>

int main() {
    // Augmented matrix [A|b]
    double mat[2][3] = {
        {3, -1, 3},   // 3x - y = 3
        {4, -1, 8}    // 4x - y = 8
    };

    // Row operation: R2 -> R2 - (4/3)R1
    double factor = mat[1][0] / mat[0][0];
    for (int j = 0; j < 3; j++) {
        mat[1][j] = mat[1][j] - factor * mat[0][j];
    }

    // Scale R2 to make pivot = 1
    double scale = mat[1][1];
    for (int j = 0; j < 3; j++) {
        mat[1][j] /= scale;
    }

    // Back substitution
    double y = mat[1][2];
    double x = (mat[0][2] - mat[0][1] * y) / mat[0][0];

    printf("x = %.2f\n", x);
    printf("y = %.2f\n", y);
    printf("Fraction = %.2f/%.2f\n", x, y);

    return 0;
}


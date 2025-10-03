#include <stdio.h>
#include <math.h>

int main() {
    double A[2][2];
    double a, b, c; // coefficients for quadratic
    double D, k1, k2;

    // Input matrix
    printf("Enter the 2x2 matrix elements:\n");
    for(int i=0; i<2; i++) {
        for(int j=0; j<2; j++) {
            scanf("%lf", &A[i][j]);
        }
    }

    // Expecting matrix of form [[k, 8], [1, 2k]]
    // General quadratic from determinant:
    // det = A[0][0]*A[1][1] - A[0][1]*A[1][0]
    // => k*(2k) - 8*1 = 2k^2 - 8 = 0

    a = 2;
    b = 0;
    c = -8;

    // Discriminant
    D = b*b - 4*a*c;

    if (D < 0) {
        printf("No real values of k\n");
    } else {
        k1 = (-b + sqrt(D)) / (2*a);
        k2 = (-b - sqrt(D)) / (2*a);

        printf("Equation: 2k^2 - 8 = 0\n");
        printf("Values of k for which matrix is singular:\n");
        printf("k = %.2f\n", k1);
        printf("k = %.2f\n", k2);
    }

    return 0;
}


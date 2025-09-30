#include <stdio.h>
#include <math.h>

// Dot product of 3D vectors
double dot(double a[3], double b[3]) {
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2];
}

// Print vector in matrix row form
void print_vec(double v[3]) {
    printf("[ %.3f  %.3f  %.3f ]", v[0], v[1], v[2]);
}

int main() {
    // Given plane parameters
    double n1[3] = {1, 3, 0};
    double n2[3] = {3, -1, -4};
    double c1 = -6, c2 = 0;

    // Inner products
    double n1n1 = dot(n1, n1);   // 10
    double n1n2 = dot(n1, n2);   // 0
    double n2n2 = dot(n2, n2);   // 26

    printf("n1·n1 = %.0f, n1·n2 = %.0f, n2·n2 = %.0f\n", n1n1, n1n2, n2n2);

    // Quadratic: (c1+λc2)^2 = n1·n1 + 2λ n1·n2 + λ^2 n2·n2
    // => (c2^2 - n2n2) λ^2 + (2c1c2 - 2n1n2) λ + (c1^2 - n1n1) = 0

    double A = c2*c2 - n2n2;
    double B = 2*c1*c2 - 2*n1n2;
    double C = c1*c1 - n1n1;

    printf("Quadratic: %.0f λ^2 + %.0f λ + %.0f = 0\n", A, B, C);

    double disc = B*B - 4*A*C;
    if (disc < 0) {
        printf("No real solutions for λ.\n");
        return 0;
    }

    double lambda1 = (-B + sqrt(disc)) / (2*A);
    double lambda2 = (-B - sqrt(disc)) / (2*A);

    printf("Solutions: λ1 = %.3f, λ2 = %.3f\n", lambda1, lambda2);

    // Compute normals for each λ
    double n_case1[3], n_case2[3];
    for(int i=0; i<3; i++) {
        n_case1[i] = (n1[i] + lambda1*n2[i]) / (c1 + lambda1*c2);
        n_case2[i] = (n1[i] + lambda2*n2[i]) / (c1 + lambda2*c2);
    }

    printf("\nEquation of required planes:\n");

    printf("1) ");
    print_vec(n_case1);
    printf(" * x = 1\n");

    printf("2) ");
    print_vec(n_case2);
    printf(" * x = 1\n");

    return 0;
}


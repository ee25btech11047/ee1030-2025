#include <stdio.h>
#include <math.h>

int main() {
    // Given points
    double A[2] = {-3, 4};
    double B[2] = {5, 4};

    // Solve equations for center
    // x = 1
    // x - 4y = -7
    double x = 1;
    double y = (x + 7) / 4.0;

    double O[2] = {x, y};
    printf("Center O = (%.2f, %.2f)\n", O[0], O[1]);

    // Opposite vertices
    double C[2] = {2*O[0] - A[0], 2*O[1] - A[1]};
    double D[2] = {2*O[0] - B[0], 2*O[1] - B[1]};

    printf("C = (%.2f, %.2f)\n", C[0], C[1]);
    printf("D = (%.2f, %.2f)\n", D[0], D[1]);

    // Side vectors
    double AB[2] = {B[0]-A[0], B[1]-A[1]};
    double AD[2] = {D[0]-A[0], D[1]-A[1]};

    // Cross product (2D determinant)
    double area = fabs(AB[0]*AD[1] - AB[1]*AD[0]);
    printf("Area of rectangle = %.2f\n", area);

    return 0;
}

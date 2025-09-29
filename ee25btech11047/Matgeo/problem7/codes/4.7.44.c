#include <stdio.h>
#include <math.h>

int main() {
    // Plane normal vector components
    double n[3] = {2.0/7.0, 3.0/7.0, -6.0/7.0};

    // Point (origin)
    double x[3] = {0.0, 0.0, 0.0};

    // Compute n^T x
    double dot = 0.0;
    for (int i = 0; i < 3; i++) {
        dot += n[i] * x[i];
    }

    // Numerator = |n^T x - 1|
    double numerator = fabs(dot - 1.0);

    // Denominator = ||n||
    double norm = sqrt(n[0]*n[0] + n[1]*n[1] + n[2]*n[2]);

    // Distance
    double d = numerator / norm;

    printf("The distance of the plane from the origin is: %.2f\n", d);

    return 0;
}

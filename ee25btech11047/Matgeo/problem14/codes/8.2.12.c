#include <stdio.h>
#include <math.h>

int main() {
    // Conic: 36x^2 + 4y^2 = 144
    double V[2][2] = {{36,0},{0,4}};
    double u[2] = {0,0};
    double f = -144;

    // Step 1: eigenvalues (already diagonal since V is diagonal)
    double lam1 = 4;   // smaller eigenvalue (after swap)
    double lam2 = 36;  // larger eigenvalue

    // Step 2: compute f0
    double f0 = -(f);   // since u=0, f0 = -f
    printf("f0 = %.2f\n", f0);

    // Step 3: eccentricity
    double e = sqrt(1 - lam1/lam2);
    printf("Eccentricity e = %.5f\n", e);

    // Step 4: semi-axes
    double a = sqrt(f0/lam1);
    double b = sqrt(f0/lam2);
    printf("Semi-major axis a = %.2f\n", a);
    printf("Semi-minor axis b = %.2f\n", b);

    // Step 5: vertices
    printf("Vertices (major): (%.2f,0), (%.2f,0)\n", a, -a);
    printf("Vertices (minor): (0,%.2f), (0,%.2f)\n", b, -b);

    // Step 6: directrix constant c (matrix formula simplified)
    double c = (1/e) * sqrt((lam2 * f0)/lam1);
    printf("Directrix constant c = ±%.2f\n", c);

    // Directrix equations (for n = (0,6))
    printf("Directrices: y = ±%.2f\n", c/6.0);

    // Step 7: foci
    double Fy = (c * e * e / lam2) * 6.0;  // factor 6 from n=(0,6)
    printf("Foci: (0,%.2f), (0,%.2f)\n", Fy, -Fy);

    // Step 8: latus rectum length
    double l = (2 * sqrt(f0 * lam1)) / lam2;
    printf("Latus rectum length = %.2f\n", l);

    return 0;
}


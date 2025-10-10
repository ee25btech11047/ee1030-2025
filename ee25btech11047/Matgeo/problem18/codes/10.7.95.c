#include <stdio.h>
#include <math.h>

int main() {
    double a = 3.0;
    double L = 2.0 * sqrt(7.0);
    double r = sqrt(a*a + (L/2)*(L/2));
    double f = a*a + (L/2)*(L/2) - r*r;

    double centers[4][2] = {
        { a,  r},
        { a, -r},
        {-a,  r},
        {-a, -r}
    };

    for(int i=0; i<4; i++) {
        double h = centers[i][0];
        double k = centers[i][1];
        printf("Circle %d: Centre = (%.2f, %.2f), Radius = %.2f\n", i+1, h, k, r);
    }

    printf("Constant term f = %.2f\n", f);
    return 0;
}


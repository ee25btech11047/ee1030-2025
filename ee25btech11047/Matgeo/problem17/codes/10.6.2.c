// tangent_circle.c
// Tangent points from an external point to a circle
#include <stdio.h>
#include <math.h>

// Tangent function to be called from Python
void tangent_points(double r, double px, double py, double *Ax, double *Ay, double *Bx, double *By) {
    double ox = 0.0, oy = 0.0;
    double d = sqrt((px - ox)*(px - ox) + (py - oy)*(py - oy));

    if (d <= r) {
        *Ax = *Ay = *Bx = *By = NAN;
        return;
    }

    double r2 = r*r;
    double d2 = d*d;
    double k = r2 / d2;
    double h = (r / d2) * sqrt(d2 - r2);

    *Ax = k*px - h*py;
    *Ay = k*py + h*px;
    *Bx = k*px + h*py;
    *By = k*py - h*px;
}


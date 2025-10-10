#include <stdio.h>
#include <math.h>

// Function g(h)
double g(double h[2], double V[2][2], double u[2], double f) {
    double temp1 = h[0]*(V[0][0]*h[0] + V[0][1]*h[1]) + 
                   h[1]*(V[1][0]*h[0] + V[1][1]*h[1]);
    double temp2 = 2*(u[0]*h[0] + u[1]*h[1]);
    return temp1 + temp2 + f;
}

int main() {
    // Conic parameters for y^2 = x
    double V[2][2] = {{0,0},{0,1}};
    double u[2] = {-0.5,0};
    double f = 0;

    // Line parameters x = h + k*m  (x = 2y)
    double h[2] = {0,0};
    double m[2] = {2,1};

    // Compute intersections using formula
    double mtVm = m[0]*(V[0][0]*m[0] + V[0][1]*m[1]) +
                  m[1]*(V[1][0]*m[0] + V[1][1]*m[1]);

    double Vh_u[2] = {V[0][0]*h[0] + V[0][1]*h[1] + u[0],
                      V[1][0]*h[0] + V[1][1]*h[1] + u[1]};
    double mVu = m[0]*Vh_u[0] + m[1]*Vh_u[1];
    double disc = mVu*mVu - g(h,V,u,f)*mtVm;

    double kappa1 = (-mVu + sqrt(disc))/mtVm;
    double kappa2 = (-mVu - sqrt(disc))/mtVm;

    double x1[2] = {h[0] + kappa1*m[0], h[1] + kappa1*m[1]};
    double x2[2] = {h[0] + kappa2*m[0], h[1] + kappa2*m[1]};

    printf("Intersection points:\n");
    printf("x1 = (%.2f, %.2f)\n", x1[0], x1[1]);
    printf("x2 = (%.2f, %.2f)\n", x2[0], x2[1]);

    // Area bounded (integral from y=0 to y=2 of (2y - y^2) dy)
    double area = (pow(2,2) - pow(2,3)/3.0) - (0 - 0);
    printf("Bounded Area = %.4f\n", area);

    // Generate data for plotting
    FILE *fp = fopen("parabola_line.dat","w");
    if(fp == NULL) {
        printf("Error opening file.\n");
        return 1;
    }

    // Parabola points
    for(double y=-3; y<=3; y+=0.05) {
        double x = y*y;
        fprintf(fp,"%lf %lf P\n",x,y);  // P for parabola
    }

    // Line points
    for(double y=-3; y<=3; y+=0.05) {
        double x = 2*y;
        fprintf(fp,"%lf %lf L\n",x,y);  // L for line
    }

    fclose(fp);
    printf("Data written to parabola_line.dat (columns: x y label).\n");
    printf("Use gnuplot to plot:\n");
    printf("  plot 'parabola_line.dat' using 1:2:(stringcolumn(3)) with labels\n");

    return 0;
}


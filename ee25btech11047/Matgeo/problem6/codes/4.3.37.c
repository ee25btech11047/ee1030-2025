#include <stdio.h>

int main() {
    // Points A and B
    int Ax = 1, Ay = 2;
    int Bx = 3, By = 6;

    // Direction vector of AB
    int dx = Bx - Ax;
    int dy = By - Ay;

    // Normal vector (perpendicular to direction)
    int nx = -dy;
    int ny = dx;

    // Equation: n^T * x = c
    // Compute c using point A
    int c = nx * Ax + ny * Ay;

    printf("Normal vector n = (%d, %d)\n", nx, ny);
    printf("Equation of line: %d*x + %d*y = %d\n", nx, ny, c);

    // Convert to slope-intercept form if ny != 0
    if (ny != 0) {
        double slope = -(double)nx / ny;
        double intercept = (double)c / ny;
        printf("Line equation (y = mx + c): y = %.2fx + %.2f\n", slope, intercept);
    }

    return 0;
}

#include <stdio.h>
#include <math.h>

// Define 3D vector structure
typedef struct {
    double x, y, z;
} Vector;

// Cross product
Vector cross(Vector a, Vector b) {
    Vector result;
    result.x = a.y * b.z - a.z * b.y;
    result.y = a.z * b.x - a.x * b.z;
    result.z = a.x * b.y - a.y * b.x;
    return result;
}

// Dot product
double dot(Vector a, Vector b) {
    return a.x * b.x + a.y * b.y + a.z * b.z;
}

// Function to test the conditions (returns int results for options a–d)
void check_conditions(Vector a, Vector b, Vector c, int *results) {
    Vector ab = cross(a, b);
    Vector bc = cross(b, c);
    Vector ca = cross(c, a);

    // Option (a): all cross products = 0
    results[0] = (ab.x==0 && ab.y==0 && ab.z==0 &&
                  bc.x==0 && bc.y==0 && bc.z==0 &&
                  ca.x==0 && ca.y==0 && ca.z==0);

    // Option (b): all equal and nonzero
    results[1] = ((ab.x==bc.x && ab.y==bc.y && ab.z==bc.z) &&
                  (bc.x==ca.x && bc.y==ca.y && bc.z==ca.z) &&
                  !(ab.x==0 && ab.y==0 && ab.z==0));

    // Option (c): ab = bc = a×c ≠ 0
    Vector ac = cross(a, c);
    results[2] = ((ab.x==bc.x && ab.y==bc.y && ab.z==bc.z) &&
                  (bc.x==ac.x && bc.y==ac.y && bc.z==ac.z) &&
                  !(ab.x==0 && ab.y==0 && ab.z==0));

    // Option (d): ab, bc, ca mutually perpendicular (dot = 0)
    results[3] = (fabs(dot(ab, bc)) < 1e-9 &&
                  fabs(dot(bc, ca)) < 1e-9 &&
                  fabs(dot(ca, ab)) < 1e-9);
}


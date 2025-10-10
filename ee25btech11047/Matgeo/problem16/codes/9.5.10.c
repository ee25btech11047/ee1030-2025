#include <stdio.h>
#include <math.h>

int main() {
    // Given conic: 2x^2 - k√2 x + 1 = 0
    // Matrices and vectors as per conic representation:
    // x^T V x + 2u^T x + f = 0

    double V[2][2] = {{2, 0}, {0, 0}};
    double h[2] = {0, 0};
    double m[2] = {1, 0};
    double f = 1;
    double k;       // unknown to be determined

    // Given condition: (sum of roots) = √2
    double given_sum = sqrt(2);

    // From formula:
    // κ₁ + κ₂ = -[2 * (mᵀ(Vh + u))] / (mᵀ V m)
    // For given h = 0, m = [1 0]ᵀ :
    // mᵀ V m = 2,  (Vh + u) = [-k√2/2, 0]ᵀ
    // ⇒ κ₁ + κ₂ = -[2 * (-k√2/2)] / 2 = (k√2)/2

    // Equating to given sum √2 ⇒ (k√2)/2 = √2 ⇒ k = 2

    k = 2.0;

    // Verification step:
    double u[2] = { -k * sqrt(2) / 2.0, 0.0 };
    double Vh_plus_u[2];
    Vh_plus_u[0] = V[0][0]*h[0] + V[0][1]*h[1] + u[0];
    Vh_plus_u[1] = V[1][0]*h[0] + V[1][1]*h[1] + u[1];

    double mT_V_m = m[0]*(V[0][0]*m[0] + V[0][1]*m[1]) +
                    m[1]*(V[1][0]*m[0] + V[1][1]*m[1]);

    double mT_Vh_u = m[0]*Vh_plus_u[0] + m[1]*Vh_plus_u[1];

    double kappa_sum = -2 * mT_Vh_u / mT_V_m;

    printf("Computed κ₁ + κ₂ = %.4f\n", kappa_sum);
    printf("Given sum of roots = %.4f\n", given_sum);
    printf("Value of k = %.2f\n", k);

    return 0;
}


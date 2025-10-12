#include <stdio.h>
#include <math.h>

#define N 4
#define EPS 1e-9  // Tolerance for floating-point comparison

int main() {
    double L[N][N] = {
        {3, -1, -1, -1},
        {-1, 2, -1, 0},
        {-1, -1, 3, 0},
        {-1, 0, -1, 1}
    };
    double b[N] = {1, 1, 1, 1};
    double A[N][N];
    int i, j, k;

    // Copy L to A (to preserve original)
    for (i = 0; i < N; i++)
        for (j = 0; j < N; j++)
            A[i][j] = L[i][j];

    // Step 1: Row reduction to find rank
    int rank = N;
    for (i = 0; i < rank; i++) {
        // If diagonal element is zero, try to swap with a lower row
        if (fabs(A[i][i]) < EPS) {
            int swap_row = i + 1;
            while (swap_row < rank && fabs(A[swap_row][i]) < EPS)
                swap_row++;
            if (swap_row == rank) {
                rank--;
                for (k = 0; k < N; k++)
                    A[k][i] = A[k][rank];
                i--;
                continue;
            }
            // Swap rows
            for (j = 0; j < N; j++) {
                double temp = A[i][j];
                A[i][j] = A[swap_row][j];
                A[swap_row][j] = temp;
            }
        }

        // Eliminate below
        for (j = i + 1; j < N; j++) {
            double factor = A[j][i] / A[i][i];
            for (k = 0; k < N; k++)
                A[j][k] -= factor * A[i][k];
        }
    }

    // Count non-zero rows
    int non_zero_rows = 0;
    for (i = 0; i < N; i++) {
        int non_zero = 0;
        for (j = 0; j < N; j++) {
            if (fabs(A[i][j]) > EPS) {
                non_zero = 1;
                break;
            }
        }
        if (non_zero) non_zero_rows++;
    }
    rank = non_zero_rows;

    // Step 2: Check for zero row after adding all rows
    double R1[4];
    for (j = 0; j < 4; j++)
        R1[j] = L[0][j] + L[1][j] + L[2][j] + L[3][j];

    int zero_row = 1;
    for (j = 0; j < 4; j++)
        if (fabs(R1[j]) > EPS)
            zero_row = 0;

    // Step 3: Compatibility condition
    double sum_b = 0;
    for (i = 0; i < N; i++)
        sum_b += b[i];

    // Step 4: Print results
    if (zero_row)
        printf("Option a) TRUE\n");
    else
        printf("Option a) FALSE\n");

    if (rank == 4)
        printf("Option b) TRUE\n");
    else
        printf("Option b) FALSE\n");

    if (fabs(sum_b) < EPS)
        printf("Option c) TRUE\n");
    else
        printf("Option c) FALSE\n");

    if (rank == 3)
        printf("Option d) TRUE\n");
    else
        printf("Option d) FALSE\n");

    // Optional: Print computed rank
    printf("\nComputed rank of L = %d\n", rank);

    return 0;
}

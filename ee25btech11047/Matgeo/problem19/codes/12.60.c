#include <stdio.h>

#define N 3  // size of the square matrix

int main() {
    int B[N][N] = {
        {0, 2, -1},
        {-2, 0, 3},
        {1, -3, 0}
    };
    
    int isSkewSymmetric = 1;  // 1 = true, 0 = false

    // Check the transpose property B^T = -B
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (B[i][j] != -B[j][i]) {
                isSkewSymmetric = 0;
                break;
            }
        }
        if (!isSkewSymmetric) break;
    }

    // Print the matrix
    printf("Matrix B:\n");
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            printf("%4d", B[i][j]);
        }
        printf("\n");
    }

    // Print result as 1 or 0
    printf("\nIs B skew-symmetric (B^T = -B)? %d\n", isSkewSymmetric);

    return 0;
}

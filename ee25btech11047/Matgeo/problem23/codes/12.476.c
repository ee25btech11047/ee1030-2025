#include <stdio.h>

#define N 3  // size of the square matrices

// Function to multiply two matrices
void multiply(int A[N][N], int B[N][N], int C[N][N]) {
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            C[i][j] = 0;
            for(int k=0; k<N; k++)
                C[i][j] += A[i][k] * B[k][j];
        }
    }
}

// Function to print a matrix
void printMatrix(int M[N][N]) {
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++)
            printf("%d ", M[i][j]);
        printf("\n");
    }
}

int main() {
    // Example matrices
    int A[N][N] = {{1,0,0},{0,1,0},{0,0,1}};
    int B[N][N] = {{1,0,0},{0,1,0},{0,0,1}}; // B = inverse of A (identity in this case)
    int C[N][N];

    multiply(A, B, C);

    printf("Matrix AB:\n");
    printMatrix(C);

    // Check if C is identity
    int isIdentity = 1;
    for(int i=0;i<N;i++)
        for(int j=0;j<N;j++)
            if((i==j && C[i][j]!=1) || (i!=j && C[i][j]!=0))
                isIdentity = 0;

    if(isIdentity)
        printf("Hence, B = A^-1\n");
    else
        printf("B is NOT the inverse of A\n");

    return 0;
}

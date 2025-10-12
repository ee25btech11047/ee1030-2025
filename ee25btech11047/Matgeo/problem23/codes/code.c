#include <stdio.h>
#include <stdlib.h>

#define N 3

// Multiply two N x N matrices
void multiply(double A[N][N], double B[N][N], double C[N][N]) {
    for(int i=0;i<N;i++) {
        for(int j=0;j<N;j++) {
            C[i][j] = 0.0;
            for(int k=0;k<N;k++)
                C[i][j] += A[i][k] * B[k][j];
        }
    }
}

// Check if a matrix is identity
int is_identity(double M[N][N]) {
    for(int i=0;i<N;i++)
        for(int j=0;j<N;j++)
            if((i==j && M[i][j]<0.999 || M[i][j]>1.001) || (i!=j && (M[i][j]<-0.001 || M[i][j]>0.001)))
                return 0;
    return 1;
}

// Function to verify if B is inverse of A
int verify_inverse(double A[N][N], double B[N][N]) {
    double C[N][N];
    multiply(A, B, C);
    return is_identity(C);
}

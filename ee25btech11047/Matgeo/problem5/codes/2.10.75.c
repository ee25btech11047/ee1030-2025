#include <stdio.h>

// Function to compute rank of an n x 2 matrix
// Since columns are multiples, rank is at most 1
int rankMatrix(int n, int col1[], int col2[]) {
    int i;
    // check if both columns are zero
    int zero1 = 1, zero2 = 1;
    for(i=0; i<n; i++) {
        if(col1[i] != 0) zero1 = 0;
        if(col2[i] != 0) zero2 = 0;
    }
    if(zero1 && zero2) return 0; // zero matrix
    // check if col2 is multiple of col1
    int ratio_num = 0, ratio_den = 0;
    for(i=0; i<n; i++) {
        if(col1[i] != 0) {
            ratio_num = col2[i];
            ratio_den = col1[i];
            break;
        }
    }
    int dep = 1;
    for(i=0; i<n; i++) {
        if(col1[i]*ratio_num != col2[i]*ratio_den) {
            dep = 0;
            break;
        }
    }
    if(dep) return 1; // dependent columns
    return 2; // independent (won’t happen here)
}

int main() {
    int n, k, i;

    printf("Enter dimension n: ");
    scanf("%d", &n);

    int a[n], b[n];
    printf("Enter vector a (%d values): ", n);
    for(i=0; i<n; i++) scanf("%d", &a[i]);

    printf("Enter vector b (%d values): ", n);
    for(i=0; i<n; i++) scanf("%d", &b[i]);

    printf("Enter value of k: ");
    scanf("%d", &k);

    int col1[n], col2[n];
    for(i=0; i<n; i++) {
        col1[i] = 2*b[i];          // P - Q
        col2[i] = (k-1)*b[i];      // R - P
    }

    printf("Matrix M = [col1 | col2]\n");
    for(i=0; i<n; i++) {
        printf("[%d  %d]\n", col1[i], col2[i]);
    }

    int r = rankMatrix(n, col1, col2);
    printf("Rank(M) = %d\n", r);

    if(r <= 1) {
        printf("=> Points are collinear\n");
    } else {
        printf("=> Points are not collinear\n");
    }

    return 0;
}

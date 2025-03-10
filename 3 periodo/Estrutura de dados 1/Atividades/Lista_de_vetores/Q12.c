#include <stdio.h>

int main(){

    int A[10] = {1,3,5,7,9,11,13,15,17,19}, B[10] = {2,4,6,8,10,12,14,16,18,20}, C[20];
    int *P1 = A, *P2 = B;


    for (int i = 0; i < 20; i++)
    {
        if (i % 2 == 0)
        {
            C[i] = *P1;
            P1++;
        }
        else{
            C[i] = *P2;
            P2++;
        }
        
        printf("%d ", C[i]);
    }
    
    return 0;
}
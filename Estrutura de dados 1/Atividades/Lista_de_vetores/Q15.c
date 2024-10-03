#include <stdio.h>
#include <stdbool.h>

#define TAM 10


bool verificar_permutacao(int A[], int B[])
{
    for (int i = 0; i < TAM; i++)
    {
        if (A[i] == B[TAM -1 - i])
        {
            return false;
        }
    }
    
    return true;
}

int main()
{
    int A[TAM], B[TAM];

    printf("A\n");
    for (int i = 0; i < TAM; i++)
    {
        scanf("%d", &A[i]);
    }

    printf("\nB\n");
    for (int i = 0; i < TAM; i++)
    {
        scanf("%d", &A[i]);
    }

    if (verificar_permutacao(A,B))
    {
        printf("\nSim");
    }
    else{
        printf("\nNao");
    }
    
    return 0;
}
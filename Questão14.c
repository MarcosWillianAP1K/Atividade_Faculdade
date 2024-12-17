#include <stdio.h>
#include <stdlib.h>


int *vetor()
{
    int *vet = (int *)malloc(5 * sizeof(int));


    for (int i = 0; i < 5; i++)
    {
        vet[i] = i+1;
    }

    return vet;
}


int main()
{
    int *vet = vetor();

    for (int i = 0; i < 5; i++)
    {
        printf("%d ", vet[i]);
    }

    return 0;
}
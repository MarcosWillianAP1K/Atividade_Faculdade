#include <stdio.h>
#include <stdlib.h>
#include <time.h>
int main(){

    int vet[20], soma = 0;

    for (int i = 0; i < 20; i++)
    {
        vet[i] = rand() % 21;

        if (vet[i] % 2 == 0)
        {
            soma += vet[i];
        }
        
        printf("%d ", vet[i]);
    }

    printf("\n%d", soma);

    return 0;
}
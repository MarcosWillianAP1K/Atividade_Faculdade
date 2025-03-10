#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define TAM 10

bool verificar_palindromo(int vet[]){
    for (int i = 0; i < TAM / 2; i++)
    {
        if(vet[i] != vet[TAM -1 - i])
        {
            return false;
        }
    }

    return true;
}

int main()
{
    int vet[TAM];

    for (int i = 0; i < TAM; i++)
    {
        scanf("%d", &vet[i]);
    }

    if (verificar_palindromo(vet))
    {
        printf("\nSim");
    }
    else{
        printf("\nNão");
    }

    return 0;
}
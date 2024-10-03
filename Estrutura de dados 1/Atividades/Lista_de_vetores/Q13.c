#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>

#define TAM 10


bool verificar_se_e_repetido(int vet[], int *posicao)
{
    for (int i = *posicao - 1; i >= 0; i--)
    {
        if (vet[*posicao] == vet[i])
        {
            return true;
        }
    }

    return false;
}


void mover(int vet[], int *posicao, int *max)
{

    for (int i = *posicao; i < *max; i++)
    {
        vet[i] = vet[i + 1];
    }
}


int retirar_indices_repetidos(int vet[], int tam){

    for (int i = 0; i < tam; i++)
    {
       if(verificar_se_e_repetido(vet, &i))
       {
            mover(vet, &i, &tam);
            i--;
            tam--;
       }

    }

    return tam;
}



int main(){

    int vet[TAM], novo_tam;

    srand(time(NULL));

    for (int i = 0; i < TAM; i++)
    {
        vet[i] = rand() % TAM + 1;

        printf("%d ", vet[i]);
    }

    novo_tam = retirar_indices_repetidos(vet, TAM);

    printf("\n\n");
    for (int i = 0; i < novo_tam; i++)
    {
        printf("%d ", vet[i]);
    }
    
    

    return 0;
}
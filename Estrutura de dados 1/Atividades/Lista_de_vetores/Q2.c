#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define tam 100

int main(){

    int vet[tam], n;

    srand(time(NULL));
    
    for (int i = 0; i < tam; i++)
    {
        vet[i] = rand() % 101;
    }

    printf("Digite um valor entre 0 e 100: ");
    scanf("%d", &n);

    for (int i = 0; i < tam; i++)
    {
        if (vet[i] <= n)
        {
            printf("Posicao: %d  Valor: %d\n", i, vet[i]);
        }
    }




    return 0;
}
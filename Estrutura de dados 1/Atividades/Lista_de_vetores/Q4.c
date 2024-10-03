#include <stdio.h>


int main(){

    int tam;

    printf("Tamanho: ");
    scanf("%d", &tam);

    int vet[tam];

    for (int i = 0; i < tam; i++)
    {
        scanf("%d", &vet[i]);
        vet[i] *= -1;
    }


    for (int i = 0; i < tam; i++)
    {
       printf("%d ", vet[i]);
    }
    

    return 0;
}
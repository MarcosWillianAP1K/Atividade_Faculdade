#include <stdio.h>


#define tam 20

int main(){

    int vet[tam];


    for (int i = 0; i < tam; i++)
    {
        vet[i] = i + 1;
    }

    for(int i = 0; i < tam; i++){
        printf("%d ", vet[i]);
    }

    printf("\n");

    for(int i = 0; i < tam / 2; i++){
        int aux;

        aux = vet[i];
        vet[i] = vet[tam-i-1];
        vet[tam-i-1] = aux;
    }


    for(int i = 0; i < tam; i++){
        printf("%d ", vet[i]);
    }


    return 0;
}
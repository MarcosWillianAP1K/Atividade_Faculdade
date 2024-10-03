#include <stdio.h>


int main(){

    int vet[30], n, cont= 0;



    for (int i = 0; i < 30; i++)
    {
        scanf("%d", &vet[i]);
    }

    scanf("%d", &n);

    for (int i = 0; i < 30; i++)
    {
        if(vet[i] % n == 0){
            vet[i] = 0;
            cont++;
        }

        printf("%d ", vet[i]);
    }

    printf("\n\nMutiplos de %d: %d", n, cont);
    
    return 0;
}
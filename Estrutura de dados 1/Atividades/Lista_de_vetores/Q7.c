#include <stdio.h>

int main(){

    int vet[1000], n, cont = 0;

    scanf("%d", &n);


    for (int i = 0; i < 1000; i++)
    {
        vet[i] = cont;
        cont++;

        if (cont == n)
        {
            cont = 0;
        }

        printf("%d ", vet[i]);
    }
    
    return 0;
}
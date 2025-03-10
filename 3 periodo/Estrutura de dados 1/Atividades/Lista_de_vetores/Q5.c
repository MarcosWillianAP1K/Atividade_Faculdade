#include <stdio.h>

#define tam 10

int main(){

    int vet[tam], n;

    scanf("%d", &n);

    vet[0] = n;
     printf("%d ", vet[0]);

    for (int i = 1; i < tam; i++)
    {
        vet[i] = vet[i -1] * 2;
        printf("%d ", vet[i]);
    }
    
    return 0;
}
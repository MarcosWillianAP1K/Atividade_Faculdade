#include <stdio.h>

#define tam 10

int vet[tam];

int main()
{

    int min, max, *pmin, *pmax;

    printf("Digite os %d valores\n", tam);

    for (int i = 0; i < tam; i++)
    {
        scanf("%d", &vet[i]);

        if (i == 0)
        {
            max = i;
            min = i;
            pmax = &vet[i];
            pmin = &vet[i];
        }

        if (vet[i] > *pmax)
        {
            pmax = &vet[i];
        }

        if (vet[i] < *pmin)
        {
            pmin = &vet[i];
        }
    }


    printf("\nMaior: %d  Posicao: %d", *pmax, pmax - vet);
    printf("\nMenor: %d  Posicao: %d", *pmin, pmin - vet);

    return 0;
}
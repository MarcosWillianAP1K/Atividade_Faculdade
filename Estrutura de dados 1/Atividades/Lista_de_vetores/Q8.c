#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

bool verificar_se_e_repetido(int vet[], int *posicao)
{
    for (int i = *posicao; i >= 0; i--)
    {
        if (vet[*posicao] == vet[i])
        {
            return true;
        }
    }

    return false;
}

bool verificar_se_tem_no_outro(int *n, int vet[])
{
    for (int i = 0; i < 10; i++)
    {
        if (*n == vet[i])
        {
            return true;
        }
    }

    return false;
}

int main()
{
    int vet1[10], vet2[10], cont = 0;

    srand(time(NULL));

    for (int i = 0; i < 10; i++)
    {
        vet1[i] = rand() % 11;
        vet2[i] = rand() % 11;
    }

    for (int i = 0; i < 10; i++)
    {
        if (!verificar_se_e_repetido(vet1, &i))
        {
            if (verificar_se_tem_no_outro(&vet1[i], vet2))
            {
                cont++;
            }
        }
    }

    for (int i = 0; i < 10; i++)
    {
        printf("%d ", vet1[i]);
    }
    printf("\n");
    for (int i = 0; i < 10; i++)
    {
        printf("%d ", vet2[i]);
    }

    printf("\n\n%d\n", cont);
    

    return 0;
}
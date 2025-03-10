#include <stdio.h>
#include <stdlib.h>

typedef struct Lista
{
    int n;
    struct Lista *proximo;
} Lista;

Lista *incrementar_na_lista(Lista *cabeca, int valor)
{
    Lista *nova_cabeca = (Lista *)malloc(sizeof(Lista) * 1);

    if (nova_cabeca != NULL)
    {
        nova_cabeca->n = valor;
        nova_cabeca->proximo = cabeca;
    }

    return nova_cabeca;
}

void preencher_lista(Lista **cabeca)
{

    for (int i = 0; i < 3; i++)
    {
        if (i != 0)
        {
            // printf("endereço atual: %p\nValor atual: %d\n\n", cabeca, cabeca->n);
        }
        *cabeca = incrementar_na_lista(*cabeca, i + 1);
        // printf("Endereço proximo: %p\nNovo valor: %d\n-------\n", *cabeca->proximo, *cabeca->n);
    }
}

void printar_lista(Lista *cabeca)
{

    Lista *corpo = cabeca;

    while (corpo->proximo != NULL)
    {
        printf("%d ", corpo->n);
        corpo = corpo->proximo;
    }

    printf("%d ", corpo->n);
}

int main()
{

    Lista *cabeca = NULL;

    preencher_lista(&cabeca);
    
    printf("\n\nendereço atual: %p\n\n", cabeca);
        
    printar_lista(cabeca);

    return 0;
}
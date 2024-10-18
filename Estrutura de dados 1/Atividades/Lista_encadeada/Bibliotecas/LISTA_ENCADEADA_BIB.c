#include "LISTA_ENCADEADA_BIB.h"
#include <time.h>

void *iniciar()
{
    return NULL;
}

void adicionar_elemento(Lista **lista, int valor)
{
    Lista *novo_no = (Lista *)malloc(sizeof(Lista));
    novo_no->numero = valor;
    novo_no->proximo = NULL;

    if (*lista == NULL)
    {
        *lista = novo_no;
    }
    else
    {
        Lista *atual = *lista;

        while (atual->proximo != NULL)
        {
            atual = atual->proximo;
        }

        atual->proximo = novo_no;
    }
}

void criar_lista(Lista **lista, int tam)
{
    Lista **atual = lista;

    for (int i = 0; i < tam; i++)
    {
        adicionar_elemento(atual, i + 1);
        atual = &(*atual)->proximo;
    }
}

void criar_lista_aleatoria(Lista **lista, int tam)
{
    Lista **atual = lista;

    srand(time(NULL));

    for (int i = 0; i < tam; i++)
    {
        adicionar_elemento(atual, rand() % tam);
        atual = &(*atual)->proximo;
    }
}

void liberar_memoria(Lista **lista)
{
    Lista **anterior = lista;

    while (*lista != NULL)
    {
        lista = &(*lista)->proximo;
        free(anterior);
        anterior = lista;
    }

    free(anterior);
}

void printar_lista(Lista *list)
{
    while (list != NULL)
    {
        printf("%d ", list->numero);
        list = list->proximo;
    }
}

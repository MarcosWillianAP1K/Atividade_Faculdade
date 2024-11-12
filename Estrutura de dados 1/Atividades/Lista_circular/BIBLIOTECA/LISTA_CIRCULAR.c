#include "LISTA_CIRCULAR.h"

LISTA_CIRCULAR *iniciar()
{
    return NULL;
}

void adicionar_elemento(LISTA_CIRCULAR **lista, int n)
{
    if (*lista == NULL)
    {
        *lista = malloc(sizeof(LISTA_CIRCULAR));
        (*lista)->numero = n;
        (*lista)->proximo = *lista;

        return;
    }

    LISTA_CIRCULAR *inicio = *lista;

    while ((*lista)->proximo != inicio)
    {
        lista = &(*lista)->proximo;
    }

    (*lista)->proximo = malloc(sizeof(LISTA_CIRCULAR));
    (*lista)->proximo->numero = n;
    (*lista)->proximo->proximo = inicio;
}

void remover_elemento(LISTA_CIRCULAR *anterior, LISTA_CIRCULAR **atual, LISTA_CIRCULAR **inicio)
{
    // cada if é um caso, e deve seguir essa ordem, e retorna para evitar rodar codigos desnecessarios

    // lista vazia
    if (*atual == NULL)
    {
        return;
    }

    // lista apenas um elemento
    if ((*atual)->proximo == *atual)
    {
        free(*inicio);

        *inicio = NULL;
        *atual = NULL;

        return;
    }

    // caso o elemento seja o inicio
    if (*atual == *inicio)
    {
        LISTA_CIRCULAR *ultimo_elemento = *atual;

        while (ultimo_elemento->proximo != *inicio)
        {
            ultimo_elemento = ultimo_elemento->proximo;
        }

        *inicio = (*inicio)->proximo;
        ultimo_elemento->proximo = *inicio;

        free(*atual);

        *atual = ultimo_elemento;

        return;
    }

    // caso o elemento seja o ultimo
    if ((*atual)->proximo == *inicio)
    {
        anterior->proximo = *inicio;
    }
    else
    {
        // caso seja o meio da lista
        anterior->proximo = (*atual)->proximo;
    }

    // vale para os ultimos dois casos
    free(*atual);

    *atual = anterior;
}

void printar_lista(LISTA_CIRCULAR *lista)
{
    if (lista == NULL)
    {
        printf("NULL\n\n");
        return;
    }

    LISTA_CIRCULAR *inicio = lista;

    printf("%d", inicio->numero);

    lista = lista->proximo;

    while (lista != inicio)
    {
        printf(" -> %d", lista->numero);
        lista = lista->proximo;
    }
    printf(" -> INICIO\n\n");
}

void liberar(LISTA_CIRCULAR **lista)
{
    if (*lista == NULL)
    {
        return;
    }

    LISTA_CIRCULAR *aux = *lista;

    do
    {
        LISTA_CIRCULAR *liberar = aux;
        aux = aux->proximo;
        free(liberar);

    } while (aux != *lista);

    *lista = NULL;
}
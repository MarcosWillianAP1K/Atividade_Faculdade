#include <stdio.h>
#include <stdlib.h>


typedef struct LISTA_CIRCULAR
{
    int numero;
    struct LISTA_CIRCULAR *proximo;
}LISTA_CIRCULAR;


LISTA_CIRCULAR *iniciar();


void adicionar_elemento(LISTA_CIRCULAR **lista, int n);


void remover_elemento(LISTA_CIRCULAR *anterior, LISTA_CIRCULAR **atual, LISTA_CIRCULAR **inicio);


void printar_lista(LISTA_CIRCULAR *lista);


void liberar(LISTA_CIRCULAR **lista);
#include <stdio.h>
#include <stdlib.h>


typedef struct Lista
{
    int numero;
    struct Lista *proximo;
} Lista;



void *iniciar();

void adicionar_elemento(Lista **lista, int valor);

void criar_lista(Lista **lista, int tam);

void criar_lista_aleatoria(Lista **lista, int tam);

void liberar_memoria(Lista **lista);

void printar_lista(Lista *list);

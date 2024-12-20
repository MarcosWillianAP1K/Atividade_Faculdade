#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


typedef struct LISTA_CIRCULAR
{
    int posicao;
    int numero;
    struct LISTA_CIRCULAR *proximo;
}LISTA_CIRCULAR;


LISTA_CIRCULAR *iniciar();


void pecorrer_lista_dando_posicao(LISTA_CIRCULAR *inicio);


void adicionar_elemento_final(LISTA_CIRCULAR **lista, int n);


void adicionar_elemento_a_frente(LISTA_CIRCULAR **lista, int n);


void adicionar_elemento_inicio(LISTA_CIRCULAR **lista, int n);


void remover_elemento(LISTA_CIRCULAR *anterior, LISTA_CIRCULAR **atual, LISTA_CIRCULAR **inicio);


void printar_lista(LISTA_CIRCULAR *lista, bool opcao);


void liberar(LISTA_CIRCULAR **lista);


void criar_lista_sequencial(LISTA_CIRCULAR **lista, int tam);


int digitar_tamanho();


void criar_lista_digitando(LISTA_CIRCULAR **lista, int tam);

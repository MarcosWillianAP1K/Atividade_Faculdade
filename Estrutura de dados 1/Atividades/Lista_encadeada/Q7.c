#include "Bibliotecas\LISTA_ENCADEADA_BIB.h"
#include <stdbool.h>

#define TAM 5

void inserir_a_frente(Lista **lista, int valor)
{
    Lista *a_ser_inserido = iniciar();

    criar_lista(&a_ser_inserido, valor);

    Lista *anterior = *lista;

    *lista = (*lista)->proximo;
    anterior->proximo = a_ser_inserido;

    while (a_ser_inserido->proximo != NULL)
    {
        a_ser_inserido = a_ser_inserido->proximo;
    }
    
    a_ser_inserido->proximo = *lista;
}

void inserir_inicio(Lista *lista, int valor, Lista **inicio)
{
    Lista *a_ser_inserido = iniciar();

    criar_lista(&a_ser_inserido, valor);

    *inicio = a_ser_inserido;

    while (a_ser_inserido->proximo != NULL)
    {
        a_ser_inserido = a_ser_inserido->proximo;
    }

    a_ser_inserido->proximo = lista;
}

void pecorrer(Lista **lista, int valor)
{
    Lista *aux = *lista;
    Lista *anterior = *lista;


    while (aux != NULL)
    {
    // printf("%p  %p\n", anterior, aux);
        // printf("\nantes");
        // printf("\nAnterior: %d   %p\nAtual: %d   %p\n", anterior->numero, *anterior, aux->numero, aux);

        if (aux->numero == valor)
        {
            if (anterior != aux)
            {
                inserir_a_frente(&anterior, valor);
                inserir_a_frente(&aux, valor);
            }
            else
            {
                inserir_inicio(aux, valor, lista);
                inserir_a_frente(&aux, valor);
            }
        }
        
            if (anterior != aux)
            {
                anterior = aux;
            }
            aux = aux->proximo;
        
        // printf("\ndepois");
        // printf("\nAnterior: %d   %p\nAtual: %d   %p\n", anterior->numero, *anterior, lista->numero, lista);
    // printf("%p  %p\n", anterior, aux);
    }

    // printf("\n\n");
    // printar_lista_modificado(inicio);
    //  printf("\n");
}

int main()
{
    Lista *list = iniciar();
    int Valor;

    criar_lista(&list, TAM);

    printar_lista(list);
    printf("\nDigite um Valor\n");
    scanf("%d", &Valor);

    printf("%p\n", list);

    pecorrer(&list, Valor);

    printf("%p\n", list);

    printar_lista(list);
    printf("\n");

    liberar_memoria(&list);

    return 0;
}
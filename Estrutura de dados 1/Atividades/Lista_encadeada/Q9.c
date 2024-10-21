#include "Bibliotecas\LISTA_ENCADEADA_BIB.h"
#include <stdbool.h>

#define TAM 3

bool comparar_vetores(int *vetor_lista, int *vetor)
{
    int tam1 = sizeof(vetor_lista) - 1;
    int tam2 = sizeof(vetor) - 1;

    if(tam1 == tam2)
    {
        for (int i = 0; i < tam1; i++)
        {
            if (vetor[i] != vetor_lista[i])
            {
                return false;
            }
        }
        return true;
    }
    return false;
}

void inverter_vetores(Lista_vetores *inicio, Lista_vetores *lista)
{
    int tam = sizeof(inicio) - 1;
    int *veto_aux = (int *)malloc(sizeof(int) * tam);

    for (int i = 0; i < tam; i++)
    {
        veto_aux[i] = inicio->vetor[i];
    }

    for (int i = 0; i < tam; i++)
    {
        inicio->vetor[i] = lista->vetor[i];
    }

    for (int i = 0; i < tam; i++)
    {
        lista->vetor[i] = veto_aux[i];
    }

    free(veto_aux);
}

void pecorrer(Lista_vetores *lista, int *vetor)
{
    Lista_vetores *inicio = lista;

    while (lista != NULL)
    { 
        if(comparar_vetores(lista->vetor, vetor))
        {
            
            inverter_vetores(inicio, lista);
        }

        lista = lista->proximo;
    }
}

int main()
{
    Lista_vetores *list = NULL;
    int Vetor1[5][TAM] = {{5, 3, 8},
                        {2, 1, 6},
                        {9, 4, 7},
                        {10, 11, 12},
                        {15, 14, 13}};

    int vetor_escolhido[3] = {9, 4, 7};

    for (int i = 0; i < 5; i++)
    {
        adicionar_vetor(&list, Vetor1[i]);
    }
    
    printar_lista_vetor(list);
    printf("\n");


    pecorrer(list, vetor_escolhido);


    printar_lista_vetor(list);
    printf("\n");

    liberar_memoria_vetor(&list);

    return 0;
}
#include "Bibliotecas\LISTA_ENCADEADA_BIB.h"
#include <stdbool.h>

#define TAM 3

bool comparar_vetores(int *vetor_lista, int *vetor)
{
    int tam1 = sizeof(vetor) - 2;
    int tam2 = sizeof(vetor_lista) - 1;

    // printf("\n");
    // for (int i = 0; i < tam1; i++)
    // {
    //     printf("%d ", vetor[i]);
    // }

    // printf("\n");
    // for (int i = 0; i < tam2; i++)
    // {
    //     printf("%d ", vetor_lista[i]);
    // }
    // printf("\n");

    bool resultado = false;

    for (int i = 0; i < tam2; i++)
    {
        if (vetor[0] == vetor_lista[i])
        {
            resultado = true;
            for (int j = 0; j < tam1; j++)
            {
                if (vetor[j] != vetor_lista[j + i])
                {
                    resultado = false;
                    break;
                }
            }
        }
    }

    // printf("%d ", resultado);
    return resultado;
}

bool comparar_elementos_vetores(int *vetor_lista, int *vetor)
{
    int tam1 = sizeof(vetor) - 2;
    int tam2 = sizeof(vetor_lista) - 1;

    for (int i = 0; i < tam1; i++)
    {
        for (int j = 0; j < tam2; j++)
        {
            if (vetor[i] == vetor_lista[j])
            {
                return true;
            }
        }
    }
    return false;
}

void elimitar_elemento(Lista_vetores *anterior, Lista_vetores *atual)
{
    anterior->proximo = atual->proximo;
    free(atual);
}

void pecorrer(Lista_vetores *lista, int *vetor)
{
    Lista_vetores *inicio = lista;

    while (lista != NULL)
    {
        if (comparar_vetores(lista->vetor, vetor))
        {

            Lista_vetores *anterior = lista;
            lista = lista->proximo;

            while (lista != NULL)
            {
                if (!comparar_elementos_vetores(lista->vetor, vetor))
                {
                    Lista_vetores *atual = lista;
                    lista = lista->proximo;
                    elimitar_elemento(anterior, atual);
                }
                else
                {
                    anterior = lista;
                    lista = lista->proximo;
                }
            }
            break;
        }
        lista = lista->proximo;
    }
}

int main()
{
    Lista_vetores *list = NULL;
    int Vetor1[5][TAM] = {{4, 2, 8},
                          {3, 1, 5},
                          {7, 6, 9},
                          {10, 12, 8},
                          {15, 14, 2}};

    int vetor_escolhido[2] = {2, 8};


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
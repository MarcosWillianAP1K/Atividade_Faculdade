#include <stdio.h>
#include <stdlib.h>

#include <stdbool.h>

#define TAM 3


typedef struct Lista_vetores
{
    int *vetor;
    struct Lista_vetores *proximo;
} Lista_vetores;



void adicionar_vetor(Lista_vetores **lista, int *vetor)
{
    Lista_vetores *novo_no = (Lista_vetores *)malloc(sizeof(Lista_vetores));

    novo_no->vetor = vetor;
    novo_no->proximo = NULL;

    if (*lista == NULL)
    {
        *lista = novo_no;
    }
    else
    {
        Lista_vetores *atual = *lista;

        while (atual->proximo != NULL)
        {
            atual = atual->proximo;
        }

        atual->proximo = novo_no;
    }
}

void liberar_memoria_vetor(Lista_vetores **lista)
{
    Lista_vetores **anterior = lista;

    while (*lista != NULL)
    {
        lista = &(*lista)->proximo;
        free(anterior);
        anterior = lista;
    }

    free(anterior);
}

void printar_lista_vetor(Lista_vetores *list)
{
    while (list != NULL)
    {
        int tam = sizeof(list->vetor) - 1;
        printf("[");
     
        for (int i = 0; i < tam; i++)
        {
            printf("%d", list->vetor[i]);
            
            if (i != tam -1)
            {
                printf(", ");
            }
        }
        printf("]  ");
        
        list = list->proximo;
    }
}

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
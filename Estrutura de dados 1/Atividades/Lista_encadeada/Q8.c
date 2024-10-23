#include "Bibliotecas\LISTA_ENCADEADA_BIB.h"
#include <string.h>

#define QUANT_NOMES 5

void inverter(Lista_de_strings *anterior, Lista_de_strings *proximo, Lista_de_strings *atual)
{
    if (anterior != atual && proximo != NULL)
    {
        char *aux = (char *)malloc(strlen(proximo->string) + 1);

        if (aux != NULL)
        {
            strcpy(aux, proximo->string);

            strcpy(proximo->string, anterior->string);
            strcpy(anterior->string, aux);

            free(aux);
        }
    }
    else
    {
        char *aux = (char *)malloc(strlen(atual->string) + 1);

        if (aux != NULL)
        {
            strcpy(aux, atual->string);

            if (anterior == atual && proximo != NULL)
            {
                strcpy(atual->string, proximo->string);
                strcpy(proximo->string, aux);
            }
            
            if ( anterior != atual && proximo == NULL)
            {
                strcpy(atual->string, anterior->string);
                strcpy(anterior->string, aux);
            }
            

            if(anterior == atual && proximo == NULL)
            {
                printf("\nSUA LISTA TEM APENAS UM VALOR\n");
            }
            
            free(aux);
        }
    }
}

void pecorrer_lista_nomes(Lista_de_strings *lista, char *nome)
{
    Lista_de_strings *anterior = lista;
    Lista_de_strings *proximo = lista->proximo;

    while (lista != NULL)
    {
        proximo = lista->proximo;

        if (strstr(lista->string, nome))
        {
            inverter(anterior, proximo, lista);
        }

        if (anterior != lista)
        {
            anterior = lista;
        }

        lista = lista->proximo;
    }
}

int main()
{
    Lista_de_strings *list = iniciar();
    char *nomes[QUANT_NOMES] = {"Leonardo", "Jose", "Erick", "Samuel", "Joao"};
    char *nome_escolhido = "Joao";

    for (int i = 0; i < QUANT_NOMES; i++)
    {
        adicionar_nomes(&list, nomes[i]);
    }

    printar_lista_nomes(list);
    printf("\n");

    pecorrer_lista_nomes(list, nome_escolhido);

    printar_lista_nomes(list);
    printf("\n");

    liberar_memoria_nomes(list);

    return 0;
}
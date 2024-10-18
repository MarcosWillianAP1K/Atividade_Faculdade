#include "Bibliotecas\LISTA_ENCADEADA_BIB.h"

#define TAM 10



void verificar_na_lista(Lista *lista)
{
    int valor = lista->numero;

    Lista *anterior = lista;

    lista = lista->proximo;

    while (lista != NULL)
    {
        // printf("Anterior:\nEndereco: %p\nValor: %d\n", anterior, anterior->numero);
        // printf("Lista:\nEndereco: %p\nValor: %d\n\n", lista, lista->numero);
        // system("pause");

        if(lista->numero == valor)
        {
            Lista *liberar = lista;

            lista = lista->proximo;
            anterior->proximo = lista;
            free(liberar);
        }
        else{
            anterior = lista;
            lista = lista->proximo;
        }

    }
}



void pecorrer_lista(Lista **lista)
{
    while (*lista != NULL)
    {
        verificar_na_lista(*lista);
        lista = &(*lista)->proximo;
    }
}





int main()
{
    Lista *list_encadeda = iniciar();

    criar_lista_aleatoria(&list_encadeda, TAM);

    printar_lista(list_encadeda);
    printf("\n");

    pecorrer_lista(&list_encadeda);

    printar_lista(list_encadeda);
    printf("\n");

    liberar_memoria(&list_encadeda);

    return 0;
}
#include "Bibliotecas\LISTA_ENCADEADA_BIB.h"

#define TAM 10

int media(Lista *lista)
{
    int soma = 0, cont = 0;

    while (lista != NULL)
    {
        soma += lista->numero;
        cont++;

        lista = lista->proximo;
    }
    return soma / cont;
}

int main()
{
    Lista *list_encadeda = iniciar();

    criar_lista(&list_encadeda, TAM);

    printar_lista(list_encadeda);
    printf("\nMedia: %d", media(list_encadeda));

    liberar_memoria(&list_encadeda);

    return 0;
}
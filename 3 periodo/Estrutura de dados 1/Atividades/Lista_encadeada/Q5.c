#include "Bibliotecas\LISTA_ENCADEADA_BIB.h"

#define TAM 5

void mesclar(Lista **lista1, Lista **lista2)
{
    if (*lista1 != NULL)
    {
        while ((*lista1)->proximo != NULL)
        {
            lista1 = &(*lista1)->proximo;
        }

        (*lista1)->proximo = *lista2;
    }
    else{
        *lista1 = *lista2;
    }
}

int main()
{
    Lista *list1 = iniciar();
    Lista *list2 = iniciar();

    criar_lista(&list1, TAM);
    criar_lista(&list2, TAM);

    printar_lista(list1);
    printf("\n");
    printar_lista(list2);
    printf("\n");

    mesclar(&list1, &list2);

    printar_lista(list1);
    printf("\n");

    liberar_memoria(list1);

    return 0;
}
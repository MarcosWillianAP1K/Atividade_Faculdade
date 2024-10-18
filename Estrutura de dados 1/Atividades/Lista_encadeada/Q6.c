#include "Bibliotecas\LISTA_ENCADEADA_BIB.h"
#include <stdbool.h>

#define TAM 5

bool verificar_se_tem_no_resultado(Lista *lista, int valor)
{
    while (lista != NULL)
    {
        if (lista->numero == valor)
        {
            return true;
        }

        lista = lista->proximo;
    }

    return false;
}

void intersecao(Lista *lista1, Lista *lista2, Lista **lista_resultado)
{
    Lista *aux = lista2;

    while (lista1 != NULL)
    {
        while (aux != NULL)
        {
            if (lista1->numero == aux->numero)
            {
                if (!(verificar_se_tem_no_resultado(*lista_resultado, lista1->numero)))
                {
                    adicionar_elemento(lista_resultado, lista1->numero);
                    lista_resultado = &(*lista_resultado)->proximo;
                }
                break;
            }

            aux = aux->proximo;
        }
        aux = lista2;

        lista1 = lista1->proximo;
    }
}

int main()
{
    Lista *list1 = iniciar();
    Lista *list2 = iniciar();
    Lista *list_resultado = iniciar();

    criar_lista(&list1, TAM);
    criar_lista_aleatoria(&list2, TAM);

    printar_lista(list1);
    printf("\n");
    printar_lista(list2);
    printf("\n");

    intersecao(list1, list2, &list_resultado);

    printar_lista(list_resultado);
    printf("\n");

    liberar_memoria(&list1);
    liberar_memoria(&list2);
    liberar_memoria(&list_resultado);

    return 0;
}
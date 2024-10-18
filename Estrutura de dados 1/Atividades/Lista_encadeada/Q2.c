#include "Bibliotecas\LISTA_ENCADEADA_BIB.h"

#define TAM 10

Lista *buscar(Lista *lista, int valor)
{
    while (lista != NULL)
    {
        if (lista->numero == valor)
        {
            return lista;
        }

        lista = lista->proximo;
    }

    return NULL;
}

int main()
{
    Lista *list_encadeda = iniciar();

    criar_lista(&list_encadeda, TAM);

    printar_lista(list_encadeda);
    printf("\n");

    int valor;

    printf("Digite um valor\n");
    scanf("%d", &valor);

    Lista *resultado = buscar(list_encadeda, valor);

    if (resultado == NULL)
    {
        printf("Valor nao esta na lista\n");
    }
    else
    {
        printf("Valor encontrado %d\n", resultado->numero);
    }

    liberar_memoria(&list_encadeda);

    return 0;
}
#include "BIBLIOTECA/LISTA_CIRCULAR.h"

void pecorrer(LISTA_CIRCULAR **inicio, int n)
{
    if (*inicio == NULL)
    {
        return;
    }

    if (n >= (*inicio)->numero)
    {
        LISTA_CIRCULAR *atual = *inicio;

        do
        {
            if (atual->numero <= n && atual->proximo->numero >= n)
            {
                // para caso seja meio da lista
                adicionar_elemento_a_frente(&atual, n);
                return;
            }
            atual = atual->proximo;

        } while (atual != *inicio);

        // caso n encontre, logo ele é maior que todos, logo acresentar no final
        adicionar_elemento_final(inicio, n);
    }
    else
    {
        // para quando n é menor que inicio, logo deve ser acrensentado no inicio
        adicionar_elemento_inicio(inicio, n);
    }
}

int main()
{
    LISTA_CIRCULAR *lista = iniciar();

    // criar a lista do sequencial
    criar_lista_sequencial(&lista, digitar_tamanho());

    // o true/false serve para printar posição ou não
    printar_lista(lista, false);

    int n;
    printf("Digite o numero para adicionar: ");
    scanf("%d", &n);

    pecorrer(&lista, n);

    printar_lista(lista, false);

    liberar(&lista);

    return 0;
}
#include "BIBLIOTECA/LISTA_CIRCULAR.h"

void buscar_numeros(LISTA_CIRCULAR **lista, int n)
{
    if (*lista == NULL)
    {
        return;
    }

    LISTA_CIRCULAR *atual = *lista;
    LISTA_CIRCULAR *anterior = atual;

    do
    {
        if (atual->numero == n)
        {
            remover_elemento(anterior, &atual, lista);
        }

        if (anterior != atual)
        {
            anterior = atual;
        }
        atual = atual->proximo;

    } while (atual != *lista && atual != NULL);
}

int main()
{

    // NA QUESTÃO PEDE PARA USAR NOMES, MAS USAREI NUMEROS MSM, MAS A IMPLEMENTAÇÃO TBM FUNCIONA COM NOMES

    LISTA_CIRCULAR *lista = iniciar();

    criar_lista_sequencial(&lista, 5);

    // o true/false serve para printar posição ou não
    printar_lista(lista, false);

    buscar_numeros(&lista, 3);

    printar_lista(lista, false);

    liberar(&lista);

    return 0;
}
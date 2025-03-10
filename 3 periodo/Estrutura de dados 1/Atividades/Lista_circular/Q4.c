#include "BIBLIOTECA/LISTA_CIRCULAR.h"

void buscar_numeros(LISTA_CIRCULAR **inicio, int n)
{
    if (*inicio == NULL)
    {
        printf("lista vazia");
        return;
    }

    printf("Num buscado: %d\n", n);

    LISTA_CIRCULAR *atual = (*inicio)->proximo;
    LISTA_CIRCULAR *anterior = *inicio;

    while (atual != *inicio && atual != NULL)
    {

        if (atual->numero == n)
        {
            remover_elemento(anterior, &atual, inicio);
        }

        if (anterior != atual)
        {
            anterior = atual;
        }
        atual = atual->proximo;
    }

    if (atual->numero == n)
    {
        remover_elemento(anterior, &atual, inicio);
    }
}

int main()
{

    // NA QUESTÃO PEDE PARA USAR NOMES, MAS USAREI NUMEROS MSM, MAS A IMPLEMENTAÇÃO TBM FUNCIONA COM NOMES, APENAS NECESSARIO MUDAR OS TIPOS

    LISTA_CIRCULAR *lista = iniciar();

    // criar a lista do tamaho e jeito q eu quiser
    criar_lista_digitando(&lista, digitar_tamanho());

    // o true/false serve para printar posição ou não
    printar_lista(lista, false);

    buscar_numeros(&lista, 3);

    printar_lista(lista, false);

    liberar(&lista);

    return 0;
}
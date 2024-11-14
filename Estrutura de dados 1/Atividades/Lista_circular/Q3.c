#include "BIBLIOTECA/LISTA_CIRCULAR.h"

void pecorrer_recursivo(LISTA_CIRCULAR *no_atual, LISTA_CIRCULAR *anterior, LISTA_CIRCULAR **inicio)
{
    // condição de parada da recursividade
    if (no_atual->proximo == *inicio)
    {
        *inicio = no_atual;

        (*inicio)->proximo = anterior;
    }
    else
    {
        pecorrer_recursivo(no_atual->proximo, no_atual, inicio);

        // quando acaba a recursivade o no volta apontando para o anterior
        no_atual->proximo = anterior;

        // na primeira chamada da função, eles são iguais, logo indicando que é o antigo primeiro elemento
        if (no_atual == anterior)
        {
            // como foi modificado o ponteiro do inicio ele é o novo inicio
            no_atual->proximo = *inicio;
        }
    }
}

void inverter_nos(LISTA_CIRCULAR **inicio)
{
    // a lista não pode estar vazia
    if (*inicio != NULL)
    {
        pecorrer_recursivo(*inicio, *inicio, inicio);
    }
}

int main()
{

    // NA QUESTÃO PEDE PARA USAR NOMES, MAS USAREI NUMEROS MSM, MAS A IMPLEMENTAÇÃO TBM FUNCIONA COM NOMES

    LISTA_CIRCULAR *lista = iniciar();

    criar_lista_sequencial(&lista, 5);

    // o true/false serve para printar posição ou não
    printar_lista(lista, false);

    inverter_nos(&lista);

    printar_lista(lista, false);

    liberar(&lista);

    return 0;
}
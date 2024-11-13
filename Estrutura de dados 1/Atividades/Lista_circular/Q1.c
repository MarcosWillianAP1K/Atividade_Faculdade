#include "BIBLIOTECA/LISTA_CIRCULAR.h"


void pecorrer(LISTA_CIRCULAR **inicio, int n)
{
    if (*inicio == NULL || n < 0)
    {
        return;
    }


    LISTA_CIRCULAR *atual = *inicio;
    //posso iniciar anterior como NULL ou atual 
    LISTA_CIRCULAR *anterior = atual;


    while (atual->proximo != atual)
    {
        for (int i = 0; i < n+1; i++)
        {
            if (atual != anterior)
            {
                anterior = atual;
            }

            atual = atual->proximo;
        }
        remover_elemento(anterior, &atual, inicio);
    }
    
}


int main()
{
    LISTA_CIRCULAR *lista = iniciar();

    criar_lista_sequencial(&lista, 5);

    //o true/false serve para printar posição ou não
    printar_lista(lista, true);


    //a posição funciona igual vetor começa do 0
    pecorrer(&lista, 1);

    printar_lista(lista, true);

    liberar(&lista);

    return 0;
}
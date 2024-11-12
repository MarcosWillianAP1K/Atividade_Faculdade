#include "BIBLIOTECA/LISTA_CIRCULAR.h"


void buscar(LISTA_CIRCULAR **inicio, int n)
{
    if (*inicio == NULL)
    {
        return;
    }

    LISTA_CIRCULAR *atual = *inicio;
    //posso iniciar anterior como NULL ou atual 
    LISTA_CIRCULAR *anterior = atual;

    do
    {
        if (atual->numero == n)
        {
            remover_elemento(anterior, &atual, inicio);
        }
        
        //atualizar anterior somente quando o atual estiver pelo menos a frente do inicio
        if (anterior != atual || anterior == NULL)
        {
            anterior = atual;
        }
        atual = atual->proximo;

    } while (atual != *inicio && atual != NULL);
    
}


int main()
{
    LISTA_CIRCULAR *lista = iniciar();

    adicionar_elemento(&lista, 1);
    adicionar_elemento(&lista, 2);
    adicionar_elemento(&lista, 3);

    printar_lista(lista);

    buscar(&lista, 3);

    printar_lista(lista);

    liberar(&lista);

    return 0;
}
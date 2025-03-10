#include "BIBLIOTECA/LISTA_CIRCULAR.h"




void modificar_lista(LISTA_CIRCULAR **inicio)
{
    LISTA_CIRCULAR *nova_lista = iniciar();
    
    LISTA_CIRCULAR *atual = *inicio;

    do
    {
        if (atual->numero % 2 == 0)
        {
            adicionar_elemento_final(&nova_lista, atual->numero);
        }

        atual = atual->proximo;
        
    } while (atual != *inicio);
    
    atual = *inicio;

    do
    {
        if (atual->numero % 2 != 0)
        {
            adicionar_elemento_final(&nova_lista, atual->numero);
        }

        atual = atual->proximo;
        
    } while (atual != *inicio);

    liberar(inicio);

    *inicio = nova_lista;
}






int main()
{
    LISTA_CIRCULAR *lista = iniciar();

    // criar a lista do sequencial
    criar_lista_sequencial(&lista, digitar_tamanho());

    // o true/false serve para printar posição ou não
    printar_lista(lista, false);

    modificar_lista(&lista);

    printar_lista(lista, false);

    liberar(&lista);

    return 0;
}
#include "BIBLIOTECA/LISTA_CIRCULAR.h"



//atual tbm n precisa de 2 ponteiros, ja que não sera o mesmo atual do pecorrer, mas oque esta a frente
void verificar(LISTA_CIRCULAR *inicio, LISTA_CIRCULAR *atual, LISTA_CIRCULAR *anterior, int n)
{
    while (atual != inicio && atual != NULL)
    {
        if (atual->numero == n)
        {
            // n tem problema inicio ser 1 ponteiro, ja que o inicio real do main nunca sera alterado
            remover_elemento(anterior, &atual, &inicio);
        }

        if (anterior != atual)
        {
            anterior = atual;
        }
        atual = atual->proximo;
    }
}


//não precisa de 2 ponteiros, ja que se tiver so um numero, n tem como ser repetido
void pecorrer(LISTA_CIRCULAR *inicio)
{
    //se tiver apenas 1 elemento n tem pq verificar
    if (inicio == NULL || inicio->proximo == inicio)
    {
        return;
    }

    LISTA_CIRCULAR *atual = inicio;
    
    do
    {   
        //posso mandar atual como anterior, ja que eu mando o o proximo do atual, logo atual seria tecnicamente o anterior
        verificar(inicio, atual->proximo, atual, atual->numero);
        
        atual = atual->proximo;

    } while (atual != inicio && atual != NULL);
}

int main()
{

    LISTA_CIRCULAR *lista = iniciar();

    // criar a lista do tamaho e jeito q eu quiser
    criar_lista_digitando(&lista, digitar_tamanho());

    // o true/false serve para printar posição ou não
    printar_lista(lista, false);

    pecorrer(lista);

    printar_lista(lista, false);

    liberar(&lista);

    return 0;
}
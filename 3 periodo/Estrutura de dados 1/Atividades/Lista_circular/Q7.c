#include "BIBLIOTECA/LISTA_CIRCULAR.h"

void pecorrer(LISTA_CIRCULAR *inicio1, LISTA_CIRCULAR *inicio2)
{
    if (inicio1 == NULL || inicio2 == NULL)
    {
        return;
    }

    //dois aux para pecorrer
    LISTA_CIRCULAR *atual1 = inicio1;
    LISTA_CIRCULAR *atual2 = inicio2;

    do
    {
        //guarda o atual2
        LISTA_CIRCULAR *anterior2 = atual2;
        //move ele para frente, para n perde o ponteiro proximo
        atual2 = atual2->proximo;

        //o anterior2 aponta pro proximo do atual1
        anterior2->proximo = atual1->proximo;
        //e o atual1 aponta para o anterior2(no caso oque eu guardei)
        atual1->proximo = anterior2;

        //pulo o no que acresentei e vou para o proximo atual1
        atual1 = atual1->proximo->proximo;

    //verificar se uma das duas listas chegaram ao fim
    } while (atual1->proximo != inicio1 && atual2->proximo != inicio2);


    //caso seja a primeira lista chegar ao fim
    if (atual1->proximo == inicio1)
    {
        //aponta para o resto da lista2
        atual1->proximo = atual2;

        //procura o fim
        while (atual2->proximo != inicio2)
        {
            atual2 = atual2->proximo;
        }
        
        //aponta pro inicio da lista1
        atual2->proximo = inicio1;
    }
    else if (atual2->proximo == inicio2)
    {
        //pro caso a lista 2 chegue ao ultimo elemento 

        //o proximo do ultimo 2, sera o proximo lista 1
        atual2->proximo = atual1->proximo;
        //e o atual 1 aponta pro atual2
        atual1->proximo = atual2;

        //como lista 1 ja aponta pro inicio 1, ja ta certo
    }

    //ajeita a contagem das posições de cada elemento
    pecorrer_lista_dando_posicao(inicio1);
}

int main()
{
    LISTA_CIRCULAR *lista1 = iniciar();
    LISTA_CIRCULAR *lista2 = iniciar();

    printf("Lista 1\n");
    criar_lista_digitando(&lista1, digitar_tamanho());

    printf("Lista 2\n");
    criar_lista_digitando(&lista2, digitar_tamanho());

    // o true/false serve para printar posição ou não
    printar_lista(lista1, false);
    printar_lista(lista2, false);


    pecorrer(lista1, lista2);

    // a lista 2 foi mesclada na lista 1
    printar_lista(lista1, false);

    liberar(&lista1);

    return 0;
}
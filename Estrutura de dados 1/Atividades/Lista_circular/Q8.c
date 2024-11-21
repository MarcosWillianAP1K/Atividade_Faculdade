#include "BIBLIOTECA/LISTA_CIRCULAR.h"

bool verificar_se_l1_esta_em_l2(LISTA_CIRCULAR *inicio1, LISTA_CIRCULAR *inicio2)
{
    if (inicio1 != NULL && inicio2 != NULL)
    {
        LISTA_CIRCULAR *atual2 = inicio2;

        do
        {
            if (atual2->numero == inicio1->numero)
            {
                LISTA_CIRCULAR *aux1 = inicio1->proximo;
                LISTA_CIRCULAR *aux2 = atual2->proximo;

                while (aux1 != inicio1 && aux2 != inicio2)
                {

                    if (aux1->numero != aux2->numero)
                    {
                        break;
                    }

                    aux1 = aux1->proximo;
                    aux2 = aux2->proximo;
                }

                if (aux1 == inicio1)
                {
                    return true;
                }
            }

            atual2 = atual2->proximo;

        } while (atual2 != inicio2);

        return false;
    }

    printf("\nUma das listas esta vazia\n");
}

int main()
{
    LISTA_CIRCULAR *lista1 = iniciar();
    LISTA_CIRCULAR *lista2 = iniciar();

    printf("Lista 1\n");
    criar_lista_digitando(&lista1, digitar_tamanho());

    printf("Lista 2\n");
    criar_lista_sequencial(&lista2, digitar_tamanho());

    // o true/false serve para printar posição ou não
    printar_lista(lista1, false);
    printar_lista(lista2, false);

    if (verificar_se_l1_esta_em_l2(lista1, lista2))
    {
        printf("\nLista 1 esta contido em lista 2\n");
    }
    else
    {
        printf("\nLista 1 nao esta contido em lista 2\n");
    }

    liberar(&lista1);
    liberar(&lista2);

    return 0;
}
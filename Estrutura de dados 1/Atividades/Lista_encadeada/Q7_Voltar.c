#include "Bibliotecas\LISTA_ENCADEADA_BIB.h"
#include <stdbool.h>

#define TAM 5


void inserir(Lista ***lista, int *valor)
{
    Lista *a_ser_inserido = NULL;

    criar_lista(&a_ser_inserido, *valor);

    Lista *proximo_no = (*(*lista))->proximo;

    (*(*lista))->proximo = a_ser_inserido;

    printf("\na_ser_inserido: %d   %p\n", a_ser_inserido->numero, a_ser_inserido );

    while (a_ser_inserido->proximo != NULL)
    {
        a_ser_inserido = a_ser_inserido->proximo;
    }
    a_ser_inserido->proximo = proximo_no;

    printf("\nproximo lista: %d   %p", (*(*lista))->proximo->numero, (*(*lista))->proximo);
    printf("\na_ser_inserido: %d   %p\n", a_ser_inserido->numero, a_ser_inserido );

    printf("\nlista antes: %d   %p   %p\n", (*(*lista))->numero, **lista , *lista);
    
    *lista = &a_ser_inserido;

    printf("\nlista depois: %d   %p   %p\n", (*(*lista))->numero, **lista , *lista);

    

}



void pecorrer(Lista **lista, int valor)
{
    Lista **anterior = lista;
    Lista *inicio = *lista;
    

    while (*lista != NULL)
    {
        printf("\nantes");
        printf("\nAnterior: %d   %p\nAtual: %d   %p   %p\n", (*anterior)->numero, *anterior, (*lista)->numero, *lista, lista);


        if ((*lista)->numero == valor && anterior != lista)
        {
            // inserir(anterior, &valor);

            //não retorna o ponteiro corretamente, não adianta
            inserir(&lista, &valor);



        }

        if (anterior != lista)
        {
            anterior = lista;
        }
            
        printf("\ndepois");
        printf("\nAnterior: %d   %p\nAtual: %d   %p   %p\n", (*anterior)->numero, *anterior, (*lista)->numero, *lista, lista);
        
    
        lista = &(*lista)->proximo;
        system("pause");
    }

    printf("\n\n");
    printar_lista_modificado(inicio);
     printf("\n");
    
}




int main()
{
    Lista *list = iniciar();
    int Valor;
  

    criar_lista(&list, TAM);


    printar_lista(list);
    printf("\nDigite um Valor\n");
    scanf("%d", &Valor);

    
    pecorrer(&list, Valor);

    
    // printar_lista(list);
    // printf("\n");

    liberar_memoria(&list);
    

    return 0;
}
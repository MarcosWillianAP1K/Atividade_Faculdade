#include <stdio.h>
#include <stdlib.h>

typedef struct lista
{
    int numero;
    struct lista *proximo;
} Lista;


void criar_lista(Lista **lista)
{
    for (int i = 0; i < 5; i++)
    {
        *lista = (Lista *)malloc(sizeof(Lista));
        (*lista)->numero = i+1;
        (*lista)->proximo = NULL;
        lista = &(*lista)->proximo;
    }
}

void printar_lista(Lista *lista)
{
    while (lista != NULL)
    {
        printf("%d -> ", lista->numero);
        lista = lista->proximo;
    }
    printf("NULL\n");
}


void liberar(Lista *lista)
{
    Lista *aux = lista;
    
    
    while (lista != NULL)
    {
        
        aux = lista;
        
        lista = lista->proximo;
        
        free(aux);
    }
    free(lista);
}



int main()
{
    Lista *lista = NULL;

    criar_lista(&lista);
    
    printar_lista(lista);
    printar_lista(lista);


    liberar(lista);



    return 0;
}

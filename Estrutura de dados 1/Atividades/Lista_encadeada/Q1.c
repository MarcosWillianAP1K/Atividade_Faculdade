
//Percebi que usaria bastante essas funções, então fiz logo uma biblioteca para evitar digitar toda hora, tem um arquivo dizendo como executar caso não saiba
#include "Bibliotecas\LISTA_ENCADEADA_BIB.h"

#define TAM 10



int contar(Lista *list){

    int cont = 0;

    while(list !=  NULL)
    {
        cont++;
        list = list->proximo;
    }

    return cont;
}

int main()
{
    Lista *list_encadeda = iniciar();

    criar_lista(&list_encadeda, TAM);
    
    printar_lista(list_encadeda); 

    printf("\nTem %d Nos", contar(list_encadeda));

    liberar_memoria(&list_encadeda);

    return 0;
}
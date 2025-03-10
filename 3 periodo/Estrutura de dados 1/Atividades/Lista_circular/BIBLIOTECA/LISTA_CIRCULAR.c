#include "LISTA_CIRCULAR.h"

LISTA_CIRCULAR *iniciar()
{
    return NULL;
}


void pecorrer_lista_dando_posicao(LISTA_CIRCULAR *inicio)
{
    if (inicio == NULL)
    {
        return;
    }
    LISTA_CIRCULAR *atual = inicio;

    int c = 0;

    do
    {
        atual->posicao = c;
        c++;
        atual = atual->proximo;
    } while (atual != inicio);
    
}


void acresentar_1_no_atual_e_proximos_nos(LISTA_CIRCULAR *atual, int posicao_de_parada)
{
    atual->posicao += 1;
    atual = atual->proximo;

    //pecorre os nos seguintes somando +1 na posição
    while (atual->posicao > posicao_de_parada)
    {
        atual->posicao += 1;
        atual = atual->proximo;
    }
}


//so funciona passando o ponteiro inicio
void adicionar_elemento_final(LISTA_CIRCULAR **lista, int n)
{
    if (*lista == NULL)
    {
        *lista = malloc(sizeof(LISTA_CIRCULAR));
        (*lista)->posicao = 0;
        (*lista)->numero = n;
        (*lista)->proximo = *lista;

        return;
    }

    int c = (*lista)->posicao + 1;

    //preciso trocar isso, melhor deixar o ** como inicio doque usar ele pra pecorrer, ja que posso modificar o inicio qunado quiser,
    //apesar que essa função n faz tanta diferença, é mais questão de boas maneiras
    LISTA_CIRCULAR *inicio = *lista;

    while ((*lista)->proximo != inicio)
    {
        c++;
        lista = &(*lista)->proximo;
    }

    (*lista)->proximo = malloc(sizeof(LISTA_CIRCULAR));
    (*lista)->proximo->posicao = c;
    (*lista)->proximo->numero = n;
    (*lista)->proximo->proximo = inicio;
}


//Ideal passar o inicio, mas deve funcionar para adicionar anterior do no atual, mas fiz com que n funcionasse, alem de mais custoso, ja que da a volta na lista
void adicionar_elemento_inicio(LISTA_CIRCULAR **inicio, int n)
{
    if (*inicio == NULL)
    {
        *inicio = malloc(sizeof(LISTA_CIRCULAR));
        (*inicio)->posicao = 0;
        (*inicio)->numero = n;
        (*inicio)->proximo = *inicio;

        return;
    }

    LISTA_CIRCULAR *fim = *inicio;

    while (fim->proximo != *inicio)
    {
        fim = fim->proximo;
    }

    //aloco pro proximo, mesmo que criar um novo no
    fim->proximo = malloc(sizeof(LISTA_CIRCULAR));
    fim->proximo->numero = n;
    fim->proximo->posicao = 0;
    fim->proximo->proximo = *inicio;
    *inicio = fim->proximo;

    acresentar_1_no_atual_e_proximos_nos((*inicio)->proximo, 0);
}


//So adiciona a frente do No atual(no caso lista)
void adicionar_elemento_a_frente(LISTA_CIRCULAR **lista, int n)
{
    if (*lista == NULL)
    {
        *lista = malloc(sizeof(LISTA_CIRCULAR));
        (*lista)->posicao = 0;
        (*lista)->numero = n;
        (*lista)->proximo = *lista;

        return;
    }
    
    LISTA_CIRCULAR *novo_no = malloc(sizeof(LISTA_CIRCULAR));
    novo_no->numero = n;
    novo_no->proximo = (*lista)->proximo;
    novo_no->posicao = (*lista)->posicao;

    (*lista)->proximo = novo_no;

    acresentar_1_no_atual_e_proximos_nos(novo_no, (*lista)->posicao);
       
}


void remover_elemento(LISTA_CIRCULAR *anterior, LISTA_CIRCULAR **atual, LISTA_CIRCULAR **inicio)
{
    // cada if é um caso, e deve seguir essa ordem, e retorna para evitar rodar codigos desnecessarios

    // lista vazia
    if (*atual == NULL)
    {
        return;
    }

    // lista apenas um elemento
    if ((*atual)->proximo == *atual)
    {
        free(*inicio);

        *inicio = NULL;
        *atual = NULL;

        return;
    }

    // caso o elemento seja o inicio
    if (*atual == *inicio)
    {
        LISTA_CIRCULAR *ultimo_elemento = *atual;

        while (ultimo_elemento->proximo != *inicio)
        {
            ultimo_elemento = ultimo_elemento->proximo;
        }

        *inicio = (*inicio)->proximo;
        ultimo_elemento->proximo = *inicio;

        free(*atual);

        *atual = ultimo_elemento;

        return;
    }

    // caso o elemento seja o ultimo
    if ((*atual)->proximo == *inicio)
    {
        anterior->proximo = *inicio;
    }
    else
    {
        // caso seja o meio da lista
        anterior->proximo = (*atual)->proximo;
    }

    // vale para os ultimos dois casos
    free(*atual);

    *atual = anterior;
}


void printar_lista(LISTA_CIRCULAR *lista, bool opcao)
{
    if (lista == NULL)
    {
        printf("NULL\n\n");
        return;
    }

    LISTA_CIRCULAR *inicio = lista;

    if (opcao)
    {
        printf("%d: ", inicio->posicao);
    }

    printf("%d", inicio->numero);

    lista = lista->proximo;

    while (lista != inicio)
    {
        printf(" -> ");

        if (opcao)
        {
            printf("%d: ", lista->posicao);
        }

        printf("%d", lista->numero);

        lista = lista->proximo;
    }
    printf(" -> INICIO\n\n");
}


void liberar(LISTA_CIRCULAR **lista)
{
    if (*lista == NULL)
    {
        return;
    }

    LISTA_CIRCULAR *aux = *lista;

    do
    {
        LISTA_CIRCULAR *liberar = aux;
        aux = aux->proximo;
        free(liberar);

    } while (aux != *lista);

    *lista = NULL;
}


void criar_lista_sequencial(LISTA_CIRCULAR **lista, int tam)
{
    for (int i = 0; i < tam; i++)
    {
        adicionar_elemento_final(lista, i + 1);
    }
}


int digitar_tamanho()
{
    printf("Digite o tamanho da lista: ");
    int n;
    scanf("%d", &n);

    printf("\n");
    return n;
}


void criar_lista_digitando(LISTA_CIRCULAR **lista, int tam)
{
    int n;
    printf("Digite uma lista de tamanho %d\n", tam);
    for (int i = 0; i < tam; i++)
    {
        scanf("%d", &n);
        adicionar_elemento_final(lista, n);
    }
    
    printf("\n\n");
}
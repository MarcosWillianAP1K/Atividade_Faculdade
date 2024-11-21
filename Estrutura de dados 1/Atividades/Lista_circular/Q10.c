#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define TAM_MAX 100

typedef struct LISTA
{
    char nome[TAM_MAX];
    int num;
    struct LISTA *proximo;
} LISTA;


bool verificar_se_ja_esta_cadastrado(LISTA *lista, int n, char *nome_da_musica)
{
    LISTA *atual = lista;

    do
    {
        
        if (strcmp(atual->nome, nome_da_musica) == 0)
        {
            atual->num += n;
            return true;
        }

        atual = atual->proximo;
    } while (atual != lista);

    return false;
}


void adicionar_elemento_final(LISTA **lista, int n, char *nome_da_musica)
{
    if (*lista == NULL)
    {
        *lista = malloc(sizeof(LISTA));
        strcpy((*lista)->nome, nome_da_musica);
        (*lista)->num = n;
        (*lista)->proximo = *lista;

        return;
    }

    if (verificar_se_ja_esta_cadastrado(*lista, n, nome_da_musica))
    {
        return;
    }
    

    // preciso trocar isso, melhor deixar o ** como inicio doque usar ele pra pecorrer, ja que posso modificar o inicio qunado quiser,
    // apesar que essa função n faz tanta diferença, é mais questão de boas maneiras
    LISTA *atual = *lista;

    while (atual->proximo != *lista)
    {
        atual = atual->proximo;
    }

    atual->proximo = malloc(sizeof(LISTA));
    strcpy(atual->proximo->nome, nome_da_musica);
    atual->proximo->num = n;
    atual->proximo->proximo = *lista;
}


void remover_elemento(LISTA *anterior, LISTA **atual, LISTA **inicio)
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
        LISTA *ultimo_elemento = *atual;

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


void remover_musicas_abaixo(LISTA **inicio, int n)
{
    if (*inicio == NULL)
    {
        printf("lista vazia");
        return;
    }

    LISTA *atual = (*inicio)->proximo;
    LISTA *anterior = *inicio;

    while (atual != *inicio && atual != NULL)
    {

        if (atual->num < n)
        {
            remover_elemento(anterior, &atual, inicio);
        }

        if (anterior != atual)
        {
            anterior = atual;
        }
        atual = atual->proximo;
    }

    if (atual->num < n)
    {
        remover_elemento(anterior, &atual, inicio);
    }
}


void liberar(LISTA **lista)
{
    if (*lista == NULL)
    {
        return;
    }

    LISTA *aux = *lista;

    do
    {
        LISTA *liberar = aux;
        aux = aux->proximo;
        free(liberar);

    } while (aux != *lista);

    *lista = NULL;
}


void printar_lista(LISTA *lista)
{
    if (lista == NULL)
    {
        printf("NULL\n\n");
        return;
    }

    LISTA *inicio = lista;


    do
    {
        printf("Nome: %s\nNum repeticoes: %d\n\n", lista->nome, lista->num);

        lista = lista->proximo;
    } while (lista != inicio);
}


char *digitar_nome()
{
    char *nome = (char *)malloc(sizeof(char) * TAM_MAX);

    if (nome == NULL)
    {
        printf("Erro ao alocar memória.\n");
        exit(1);
    }

    printf("Digite o nome: ");

    fflush(stdin);
    fgets(nome, sizeof(char) * TAM_MAX, stdin);
    fflush(stdin);

    nome[strlen(nome) - 1] = '\0';

    return nome;
}


int digitar_num()
{
    int n;

    printf("Digite o Num: ");

    if (scanf("%d", &n))
    {
        return n;
    }

    return 0;
}

int main()
{

    LISTA *lista = NULL;

    char menu;

    adicionar_elemento_final(&lista, 2, "teste");

    do
    {

        printf("1-Inserir musica\n");
        printf("2-Remover\n");
        printf("3-Imprimir playlist\n");
        printf("4-Sair\n");

        printf("Escolha: ");
        fflush(stdin);
        scanf("%c", &menu);
        fflush(stdin);
        printf("\n");

        system("cls||clear");

        switch (menu)
        {
        case '1':

            adicionar_elemento_final(&lista, digitar_num(), digitar_nome());
            system("cls||clear");
            break;

        case '2':
            printf("Remover musica a baixo de\n");
            remover_musicas_abaixo(&lista, digitar_num());
            system("cls||clear");

            break;

        case '3':
            printar_lista(lista);

            break;

        case '4':

            break;

        default:
            printf("Opcao invalida\n");
            system("pause");
            break;
        }

    } while (menu != '4');

    liberar(&lista);

    return 0;
}

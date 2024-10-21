#include <stdio.h>
#include <stdlib.h>

#define TAMANHO_VETOR 3

// Definição do nó da lista encadeada
typedef struct No {
    int vetor[TAMANHO_VETOR];
    struct No* proximo;
} No;

// Função para criar um novo nó
No* criar_no(int vetor[TAMANHO_VETOR]) {
    No* novo_no = (No*)malloc(sizeof(No));
    for (int i = 0; i < TAMANHO_VETOR; i++) {
        novo_no->vetor[i] = vetor[i];
    }
    novo_no->proximo = NULL;
    return novo_no;
}

// Função para inserir um nó no final da lista encadeada
void inserir_no_fim(No** cabeca, int vetor[TAMANHO_VETOR]) {
    No* novo_no = criar_no(vetor);
    if (*cabeca == NULL) {
        *cabeca = novo_no;
    } else {
        No* temp = *cabeca;
        while (temp->proximo != NULL) {
            temp = temp->proximo;
        }
        temp->proximo = novo_no;
    }
}

// Função para imprimir a lista encadeada
void imprimir_lista(No* cabeca) {
    No* temp = cabeca;
    int i = 1;
    while (temp != NULL) {
        printf("Vetor%d: [", i++);
        for (int j = 0; j < TAMANHO_VETOR; j++) {
            printf("%d", temp->vetor[j]);
            if (j < TAMANHO_VETOR - 1) {
                printf(", ");
            }
        }
        printf("]\n");
        temp = temp->proximo;
    }
}

// Função para reorganizar a lista encadeada
void reorganizar_lista(No** cabeca, int vetor_buscado[TAMANHO_VETOR]) {
    No *anterior = NULL, *atual = *cabeca, *encontrado = NULL, *primeiro = *cabeca;
    
    // Procurar o vetor buscado
    while (atual != NULL) {
        int encontrado_flag = 1;
        for (int i = 0; i < TAMANHO_VETOR; i++) {
            if (atual->vetor[i] != vetor_buscado[i]) {
                encontrado_flag = 0;
                break;
            }
        }
        if (encontrado_flag) {
            encontrado = atual;
            break;
        }
        anterior = atual;
        atual = atual->proximo;
    }

    // Se não encontrou o vetor, retorne
    if (encontrado == NULL) {
        printf("Vetor não encontrado.\n");
        return;
    }

    // Se o vetor buscado não for o primeiro, reorganizar a lista
    if (anterior != NULL) {
        anterior->proximo = encontrado->proximo;
        encontrado->proximo = NULL;

        // Colocar os nós anteriores ao vetor buscado no final
        No* temp = anterior->proximo ? anterior->proximo : primeiro;
        while (temp->proximo != NULL) {
            temp = temp->proximo;
        }
        temp->proximo = primeiro;
        *cabeca = encontrado;
    }
}

int main() {
    No* lista = NULL;

    // Inserir vetores na lista encadeada
    int vetor1[TAMANHO_VETOR] = {5, 3, 8};
    int vetor2[TAMANHO_VETOR] = {2, 1, 6};
    int vetor3[TAMANHO_VETOR] = {9, 4, 7};
    int vetor4[TAMANHO_VETOR] = {10, 11, 12};
    int vetor5[TAMANHO_VETOR] = {15, 14, 13};

    inserir_no_fim(&lista, vetor1);
    inserir_no_fim(&lista, vetor2);
    inserir_no_fim(&lista, vetor3);
    inserir_no_fim(&lista, vetor4);
    inserir_no_fim(&lista, vetor5);

    printf("Lista original:\n");
    imprimir_lista(lista);

    int vetor_buscado[TAMANHO_VETOR] = {9, 4, 7};

    // Reorganizar a lista com base no vetor buscado
    reorganizar_lista(&lista, vetor_buscado);

    printf("\nLista reorganizada:\n");
    imprimir_lista(lista);

    return 0;
}

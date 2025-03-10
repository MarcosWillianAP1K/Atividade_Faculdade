#include <stdio.h>
#include <stdlib.h>

void printar_torres(int n,  int A[], int B[], int C[])
{
    for (int i = n - 1; i >= 0; i--)
    {
        printf("%d\t%d\t%d\n", A[i], B[i], C[i]);
    }
    printf("A\tB\tC\n");
    printf("------------------\n");
}

void mover(char Origem, char Destino, int A[], int B[], int C[])
{
    int *Endereco_origem, *Endereco_Destino;
    int i = 0;

    if (Origem == 'A')
    {
        while (A[i++] != 0)
            ;
        Endereco_origem = &A[i - 2];
    }
    else if (Origem == 'B')
    {
        while (B[i++] != 0)
            ;
        Endereco_origem = &B[i - 2];
    }
    else if (Origem == 'C')
    {
        while (C[i++] != 0)
            ;
        Endereco_origem = &C[i - 2];
    }

    i = 0;

    if (Destino == 'A')
    {
        while (A[i++] != 0)
            ;
        Endereco_Destino = &A[i - 1];
    }
    else if (Destino == 'B')
    {
        while (B[i++] != 0)
            ;
        Endereco_Destino = &B[i - 1];
    }
    else if (Destino == 'C')
    {
        while (C[i++] != 0)
            ;
        Endereco_Destino = &C[i - 1];
    }

    *Endereco_Destino = *Endereco_origem;

    *Endereco_origem = 0;
}

void torre_de_honai(int *tam, int n, int A[], int B[], int C[], char Origem, char Destino, char Auxiliar)
{
    if (n == 1)
    {
        mover( Origem, Destino, A, B, C);

        printf("Move do %c pro %c\n", Origem, Destino);
        printar_torres(*tam, A, B, C);
        return;
    }

    torre_de_honai(tam, n - 1, A, B, C, Origem, Auxiliar, Destino);

    mover( Origem, Destino, A, B, C);
    printf("\nMove do %c pro %c\n", Origem, Destino);
    printar_torres(*tam, A, B, C);

    torre_de_honai(tam, n - 1, A, B, C, Auxiliar, Destino, Origem);
}

int main()
{

    int n;

    printf("Digite o numero de discos\n");
    scanf("%d", &n);

    int A[n + 1], B[n + 1], C[n + 1];

    for (int i = 0; i < n+1; i++)
    {
        A[i] = n - i;
        B[i] = 0;
        C[i] = 0;
    }
    A[n] = 0;

    printf("\n\n");

    printf("Torres originais\n");
    printar_torres(n, A, B, C);

    torre_de_honai(&n, n, A, B, C, 'A', 'B', 'C');

    return 0;
}
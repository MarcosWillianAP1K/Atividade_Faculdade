#include <stdio.h>
#include <stdlib.h>

int main()
{
    int N, M;

    scanf("%d %d", &N, &M);

    int **matriz = (int **)malloc(N * sizeof(int *));
    for (int i = 0; i < N; i++)
    {
        matriz[i] = (int *)malloc(M * sizeof(int));
    }

    printf("\n");

    for(int i = 0; i < N; i++)
    {
        int x;
        for(int j = 0; j < M; j++)
        {
            scanf("%d", &x);
            matriz[i][j] = x;
        }
    }

    printf("\n");

    for(int i = 0; i < N; i++)
    {
        for(int j = 0; j < M; j++)
        {
            printf("%d\t ", matriz[i][j]);
        }
        printf("\n");
    }

    for (int i = 0; i < N; i++)
    {
        free(matriz[i]);
    }
    free(matriz);

    return 0;
}
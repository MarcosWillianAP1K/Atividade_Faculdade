#include <stdio.h>

int main()
{

    int vetA[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}, vetB[10] = {10, 9, 8, 7, 6, 5, 4, 3, 2, 1}, vetC[10];

    for (int i = 0; i < 10; i++)
    {
        vetC[i] = vetA[i] + vetB[i];

        printf("%d ", vetA[i]);
    }
    printf("\n");

    for (int i = 0; i < 10; i++)
    {
        printf("%d ", vetB[i]);
    }
    printf("\n");

    for (int i = 0; i < 10; i++)
    {
        printf("%d ", vetC[i]);
    }

    return 0;
}
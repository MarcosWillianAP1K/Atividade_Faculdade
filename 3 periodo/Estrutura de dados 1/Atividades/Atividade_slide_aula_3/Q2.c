#include <stdio.h>
#include <stdlib.h>

int main()
{
    int vet[5] = {1, 2, 3, 4, 5};

    for(int i = 0; i < 5; i++)
    {
        printf("%d\n", vet[i] * 3);
    }

    return 0;
}
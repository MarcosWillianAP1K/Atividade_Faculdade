#include <stdio.h>
#include <stdlib.h>

int main()
{
    float vet[10] = {7.5, 8.0, 9.5, 6.0, 5.0, 7.0, 8.5, 9.0, 6.5, 5.5};
    float total = 0;

    for (int j = 0; j < 10; j++)
    {
        total += vet[j];
    }

    printf("Media: %.2f\n", total / 10);

    return 0;
}
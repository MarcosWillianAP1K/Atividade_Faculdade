#include <stdio.h>

int main()
{

    float vet[100], n;

    scanf("%f", &n);

    vet[0] = n;
    printf("%f ", vet[0]);

    for (int i = 1; i < 100; i++)
    {
        vet[i] = vet[i - 1] / 2;
        printf("%f ", vet[i]);
    }

    return 0;
}
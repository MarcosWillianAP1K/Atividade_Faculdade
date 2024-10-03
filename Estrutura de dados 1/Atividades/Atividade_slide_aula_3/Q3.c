#include <stdio.h>
#include <stdlib.h>

int main()
{
    int mat[3][3] = {{1, 2, 3}, 
                     {4, 5, 6}, 
                     {7, 8, 9}};
    int total;

    for(int i = 0; i < 3; i++)
    {
        total = 0;
        for(int j = 0; j < 3; j++)
        {
            total += mat[j][i];
        }

        printf("Total da coluna %d: %d\n", i, total);
    }

    return 0;
}
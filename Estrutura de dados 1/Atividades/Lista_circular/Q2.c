#include "BIBLIOTECA/LISTA_CIRCULAR.h"

bool verificar_primo(int n)
{
    for (int i = 2; i < (n / 2) + 1; i++)
    {
        if (n % i == 0 && i != n)
        {
            return false;
        }
    }
    return true;
}

void criar_lista_primos(LISTA_CIRCULAR **lista, int n)
{
    // precisa ter ao menos um numero primo
    if (n > 0)
    {
        // adiciona o primeiro
        adicionar_elemento(lista, 2);

        int cont = 1;
        // inicia com os segundo
        int primo = 3;

        while (cont < n)
        {
            if (verificar_primo(primo))
            {
                adicionar_elemento(lista, primo);
                cont++;
            }

            // pula 2 em 2
            primo += 2;
        }
    }
}

int main()
{
    LISTA_CIRCULAR *lista = iniciar();

    criar_lista_primos(&lista, 20);

    // o true/false serve para printar posição ou não
    printar_lista(lista, false);

    liberar(&lista);

    return 0;
}

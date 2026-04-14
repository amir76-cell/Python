#include <stdio.h>

int main()
{
    int n;

    printf("Entrez un nombre : ");
    scanf("%d", &n);

    if (n > 0)
    {
<<<<<<< HEAD
        printf("Le nombre est positif\n");
    }
    else if (n < 0)
    {
        printf("Le nombre est nagtif\n");
    }
    else
    {
        printf("Le nombre est nul\n");
    }

    return 0;
}

int main()
{
    int n;

    printf("Entrez un nombre : ");
    scanf("%d", &n);

    if (n == 0)
    {
        printf("Le nombre est zero (et il est pair)\n");
    }
    else if (n % 2 == 0)
    {
        printf("Le nombre est pair\n");
    }
    else
    {
        printf("Le nombre est impair\n");
    }

    return 0;
}

int main()
{
    int n;
    int fact = 1;
    printf("entrez un nombre : ");
    scanf("%d", &n);

    if (n < 0)
    {
        printf("La factorielle n'existe pas pour les nombres negatifs\n");
    }
    else
    {
        for (int i = 1; i <= n; i++)
        {
            fact = fact * i;
        }

        printf("La factorielle est : %d\n", fact);
    }

    return 0;
}
=======
        printf("Le nombre est positif");
    }
    else
    {
        printf("Le nombre est negatif");
    }

    return 0;
}
>>>>>>> f1db0169901f6b487dabc98cd059f1e9775e2954

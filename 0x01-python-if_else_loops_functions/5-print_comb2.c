#include <stdio.h>

int main(void)
{
    for(int i = 0; i <= 99; i++)
    {
        if (i <= 9)
        printf("0%d, ", i);
        else
        {
            printf("%d, ", i);
        }
    }
    return 0;
}
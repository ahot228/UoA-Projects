#include<stdio.h>
#include<stdlib.h>


int Choose(int n, int m);


int main()
{
    printf("%d", Choose(6, 2));
    return 0;
}

int Choose(int n, int m)
{
  if (m == 0 || n == m)
    {
        return 1;
    }
    else{
        return Choose(n - 1, m - 1) + Choose(n - 1, m);
    }
}
#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main(void)
{
    int x;
    printf("Large Capacity:\n");
    scanf("%d", &x);
    int y;
    printf("Small Capacity:\n");
    scanf("%d", &y);    
    int z;
    printf("Number of Items:\n");
    scanf("%d", &z);
    int large;
    large = z/x;
    int small;
    small = (z- x*large)/y;
    int scrap;
    scrap = z - x*large - y*small;
    printf("Allocated:\n - Large: %d\n - Small: %d\n - Scrap: %d\n", large, small, scrap);

    return 0;
}
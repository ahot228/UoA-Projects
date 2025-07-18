#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int LeafEater(int branch, int rest, int leaf);

int main(void)
{
    printf("Leaves eaten = %d\n", LeafEater(12, 6, 4));
    return 0;
}

int LeafEater(int branch, int rest, int leaf)
{
    int i=0;
    int j=0;
    int array[100000]={0};
    int count = 0;

    while(i<=branch){
        array[i] = 1;
        i=i+leaf;
    }
    while(j<=branch){
        if(array[j]==1){
            count++;
        }
        j=j+rest;
    }
    return count;
}
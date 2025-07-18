#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>


void ReverseArray(int *values, int left, int right);

int main(void)
{
    int values[7] = {1, 2, 3, 4, 5, 6, 7};; 
    ReverseArray(values, 1, 2); 
    for (int i = 0; i < 7; i++) { 
        printf("%d ", values[i]); 
    }
}

void ReverseArray(int *values, int left, int right)
{
    int length = right+1;
    int i, tempvalues[1000000];

    for(i = left; i < length; i++){
        tempvalues[i] = values[left+right-i];
    }
    for(i = left; i < length; i++){
        values[i] = tempvalues[i];
    }
}
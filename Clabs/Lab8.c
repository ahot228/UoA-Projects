#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int LastIndexOf(int search, int values[], int numValues);

int main(void)
{
    int values[5] = {1,2,0,2,1}; 
    int pos = LastIndexOf(2, values, 5); 
    printf("%d\n", pos);
    
    return 0;
}

int LastIndexOf(int search, int values[], int numValues)
{
    int i=0;
    int numcount=0;
    int position=0;
    while (i<numValues) {
        if (values[i] == search){
            position = i;
            numcount++;
        }
        i++;
    }
    if (numcount == 0){
        position = -1;
}
return position;
}
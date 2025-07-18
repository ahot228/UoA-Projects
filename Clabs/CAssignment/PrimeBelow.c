#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int Prime(int a);
int PrimeBelow(int upper);

int main(void)
{
    printf("Prime = %d", PrimeBelow(10));
    return 0;
}

int Prime(int a)
{
    int prime, i,b=0,count=0;   
    b=a/2;
    for(i=2; i<=b; i++) {    
        if(a%i==0){    
            prime = 0;    
            count = 1;    
            break;  
        }    
    }    
    if(count==0){
    prime = 1; 
    }
    return prime;
}

int PrimeBelow(int upper)
{
    if(upper <= 2){
    return -1;
    }
    int i, a;
    int array[1000000];
    int count = upper-1;

    for (i=0; i < upper; i++){
        array[i] = count;
        count--;
    }
    
    for(i=0; i < upper; i++){
        a = array[i];
        a = Prime(a);
        if(a == 1){
            return array[i];
        }
    }
    return -1;
}
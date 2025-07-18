#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

void RemoveLetterAt(char *word, int position);
int main(void)
{
    char word[100] = "XXX";
    RemoveLetterAt(word, 1);
    printf("Result = (%s)", word);
}

void RemoveLetterAt(char *word, int position)
{
    char temp[1000];
    int size = 0;
    int i = 0;
    while (word[i] != '\0'){
        if (i != position){
            temp[size]=word[i];
            size++;
        }
        i++;
    }
    for(i=0; i<size;i++){
        word[i] = temp[i];
    }
    word[size] = '\0';
}
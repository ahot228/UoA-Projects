#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <stdlib.h>

int OneLetterDifference(char *word1, char *word2);

int main(void)
{
    char word1[5] = "able";
    char word2[5] = "ably";

if (OneLetterDifference(word1, word2)) {
   printf("The words differ by just one character");
} else {
   printf("The words do not differ by just one character");
}
}

int OneLetterDifference(char *word1, char *word2)
{
    int i;
    int nummatch = 0;
    for(i=0; i < 4; i++){
        if(word1[i] != word2[i]){
            nummatch++;
        }
    }
    if(nummatch == 1){
        return 1;
    }else{
    return 0;
    }
}
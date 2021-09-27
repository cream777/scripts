#include <stdio.h>
#include <string.h>

char* reverser(char* string, char* stringrev){
    int i;
    int len = strlen(string);
    for (i = 0; i <= len; ++i){
        stringrev[i] = string[len - 1 - i];

    }

    return stringrev;

}


int main(){
    char string[100];
    char stringrev[strlen(string)];
    printf("\nEnter string: ");
    fgets(string, 100, stdin);
    printf("%s \n\n", reverser(string, stringrev));
    return 0;
}
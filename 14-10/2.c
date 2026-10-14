#include <stdio.h> 
char *my_strcat(char *dest, const char *src) {
    char *ptr = dest;

    while (*ptr != '\0') {
        ptr++;//moving ptr to end
    }

    while (*src != '\0') {
        *ptr = *src; //adding at the end
        ptr++;
        src++;
    }
    *ptr = '\0'; //adding null character at end

    return dest;
}
int main() {
    char str1[100];
    char str2[50];

    printf("Enter first string: "); //taking input
    scanf("%s", str1);

    printf("Enter second string: ");//taking input
    scanf("%s", str2);

    my_strcat(str1, str2);//calling function

    printf("Concatenated string: %s\n", str1);

    return 0;
}


#include "stdlib.h"
#include "stdio.h"


int solution(int H[], int N) {
    int blocks = 0;
    int *stack = malloc(N * sizeof(int));
    int stack_size = 0;
    
    for (int i = 0; i < N; i++) {
        while (stack_size && stack[stack_size] > H[i])
            stack_size --;
        if (stack_size && stack[stack_size] == H[i])
            ;
        else {
            blocks ++;
            stack_size ++;
            stack[stack_size] = H[i];
        }
    }
    free(stack);
    return blocks;
}

int main(int argc, char *argv[]) {
    int test[] = {8, 8, 5, 7, 9, 8, 7, 4, 8};
    printf("%d", solution(test, 9));
    return 0;
}



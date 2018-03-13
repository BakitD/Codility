#include <stdlib.h>

using namespace std;


int solution(int A, int B, int K) {
    int counter = 0;
    for (int i = A; i <= B; i++) 
        if (div(i, K).rem == 0) {
            counter ++;
            if (i!=1) return (B - i) / K + counter;
        }
    return counter;
}

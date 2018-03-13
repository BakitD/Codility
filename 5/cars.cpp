#include <stdlib.h>


int solution(vector<int> &A) {
    int ones = 0, zeros = 0, result = 0;
    for (vector<int>::iterator it = A.begin(); it!=A.end(); it++, ones=0)
        result += (*it) ? ((ones + 1) * zeros) : (0 * zeros++);
    return (result < 0 || result > 1000000000) ? -1 : result;
}

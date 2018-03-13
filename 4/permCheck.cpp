#include <stdlib.h>
#include <algorithm>
#include <vector>

using namespace std;

int solution(vector<int> &A) {
    sort(A.begin(), A.end());
    if (A[0] != 1) return 0;
    for (vector<int>::iterator it = A.begin(); (it+1)!=A.end(); it++)
        if (abs(*it - *(it+1)) != 1) return 0;
    return 1;
}

int main() {
  vector<int> v = {3,2};
  return solution(v);
}

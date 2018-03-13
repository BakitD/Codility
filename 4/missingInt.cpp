#include <stdlib.h>
#include <algorithm>
#include <vector>
#include <iostream>

using namespace std;

int solution(vector<int> &A) {
    sort(A.begin(), A.end());
    int n = A.size();
    vector<int>::iterator it = A.begin();
    if (n == 1) {
        if (*it == 1) return 2;
        else return 1;
    }
    if (*it > 1) return 1;
    for (; (it+1)!=A.end(); it++) {
        if (*it <= 0 && *(it + 1) > 1) return 1;
        if (*it < 0) continue;
        if (abs(*it - *(it+1)) > 1) {
            if (*(it + 1) == 1) return 2;
            if (*(it + 1) <= 0) return 1;
            return *it + 1;
        }
    }
    if (*(it) <= 0) return 1; 
    return *it + 1;
}

int main() {
  vector<int> v = {1,3,6,4,1,2};
  cout << solution(v);
  return 0;
}

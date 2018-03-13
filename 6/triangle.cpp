#include <iostream>
#include <vector>
#include <stdlib.h>

using namespace std;

int solution(vector<int> &A) {
    int n = A.size();
    if (n < 3) return 0;
    long a = 0, b = 0, c = 0;
    for (int i = 0; i < n-2; i ++)
      for (int j = i + 1; j < n-1 && A[i] > 0; j++)
        for (int k = j + 1; k < n && A[j] > 0; k++) {
            a = A[i];
            b = A[j];
            c = A[k];
            if (a + b > c && a + c > b && b + c > a) return 1;
        }
    return 0;
}

int main() {
  vector<int> v = {1,5,10};
  cout << solution(v);
  return 0;
}

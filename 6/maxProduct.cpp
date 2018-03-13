#include <vector>
#include <algorithm>
#include <stdlib.h>
#include <iostream>


using namespace std;

bool srt (int a,int b) { return (abs(a)>abs(b)); }


int solution(vector<int> &A) {
    sort(A.begin(), A.end(), srt);
    long maximal = A[0] * A[1] * A[2];
    int n = A.size();
    for (int i = 0; i < n-2; i++)
      for (int j = i + 1; j < n-1; j ++)
        for (int k = j + 1; k < n; k ++) {
            maximal = A[i] * A[j] * A[k];
            if (maximal >= 0) return maximal;
        }
    return maximal;
}

int main() {
  vector<int> v = {-3, 1, 2, -2, 5, 6};
  cout << solution(v);
  return 0;
}

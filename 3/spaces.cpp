#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int solution(vector<int> &A) {
    int n = A.size();
    if (n == 0) return 1;
    sort(A.begin(), A.end());
    int first = *A.begin();
    if (n == 1 && first == 1) return 2;
    if (first == 2 && n >= 1) return 1;
    vector<int>::iterator it = A.begin();
    for (; it+1!=A.end(); it++) if (abs(*it - *(it+1)) > 1) break;
    return (*it + 1);
}


int main() {
  vector<int> A = {1,3,5,4,2,6};
  cout << solution(A);
}

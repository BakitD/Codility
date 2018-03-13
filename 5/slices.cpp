#include <iostream>
#include <stdlib.h>
#include <vector>


using namespace std;


int solution(vector<int> &A) {
    int minimal_index = 0, n = A.size();
    float average = 0, minimal = 100000, summ = 0;
    for (int i = 0; i < n - 1; i++) {
        summ = A[i];
        for (int shift = 1; shift < n - i; shift++) {
            summ += A[i + shift];
            average = summ / (shift + 1);
            if (average < minimal) {
                minimal_index = i;
                minimal = average;
            }
        }
    }
    return minimal_index;
}


int main() {
  vector<int> v = {4, 2, 2, 5, 1, 5, 8};
  cout << solution(v);
  return 0;
}

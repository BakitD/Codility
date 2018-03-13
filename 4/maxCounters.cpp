#include <vector>

using namespace std;

vector<int> solution(int N, vector<int> &A) {
    int maximal = 0;
    int n = A.size();
    int index = 0;
    vector<int> res(N, 0);
    for (int i = 0; i < n; i++) {
        if (A[i] >= 1 && A[i] <= N) {
            index = A[i] - 1 < 0 ? A[N-1] : A[i]-1;
            maximal = (++res[index] > maximal) ? res[index] : maximal;
        }
        else if (A[i] == N + 1) fill(res.begin(), res.end(), maximal);
    }
    return res;
}

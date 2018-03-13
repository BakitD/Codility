#include <map>

using namespace std;

int solution(vector<int> &A) {
    long n = A.size();
    long result = 0;
    for (long i = 0; i < n-1; i++)
        for (long j = i+1; j < n; j++)
            result += ((i - A[i]) <= (j + A[j]) && (i + A[i]) >= (j - A[j])  ) ? 1 : 0;
    return result > 10000000 ? -1 : result;
}

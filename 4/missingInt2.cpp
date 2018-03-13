#include <vector>
#include <algorithm>

int solution(vector<int> &A) {
    sort(A.begin(), A.end());
    auto it = A.begin();
    if (*it > 1) return 1;
    for(; it!=A.end()-1; it++){
        if (*it < 0) continue;
        if (abs(*it - *(it + 1)) > 1) return *it + 1;
    }
    if (*it <= 0) return 1;
    return *(it++) + 1;
}

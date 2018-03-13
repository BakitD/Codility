#include <algorithm>
#include <set>
#include <stdlib.h>

using namespace std;

int solution(int X, vector<int> &A) {
    set<int> numbers;
    if (A.size() == 1 && A[0] != 1) return -1;
    else if (A.size() == 1 && A[0] == 1) return 0;
    for (int i = 1; i < X; i++) numbers.insert(i);
    bool flag = false;
    for (vector<int>::iterator it = A.begin(); it!=A.end(); it++) {
        if (!numbers.size()) {
            if (flag) return it - A.begin() - 1;
            if (X == *it) return it - A.begin();
        }
        set<int>::iterator fe = numbers.find(*it);
        if (fe!=numbers.end()) numbers.erase(fe);
        if (!flag) flag = *it == X;
    }
    return -1;
}

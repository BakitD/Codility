#include <vector>
#include <stdlib.h>
#include <map>
#include <algorithm>

using namespace std;

vector<int> solution(string &S, vector<int> &P, vector<int> &Q) {
    int n = P.size();
    vector<int> result;
    map<char, int> nm = {{'A', 1}, {'C', 2}, {'G', 3}, {'T', 4}};
    string::iterator it = S.begin();
    for (int i = 0; i < n; i++) result.push_back(nm[*min_element(it+P[i], it+Q[i]+1)]);
    return result;
}

int main() {
    vector<int> p = {0,0,1};
    vector<int> q = {0,1,1};
    string str = "TC";
    vector<int> result;
    result = solution(str, p, q);
    for (vector<int>::iterator it = result.begin(); it!=result.end(); it++) cout << *it;
    return 0;
}

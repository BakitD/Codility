#include <stack>
#include <vector>
#include <set>

using namespace std;

int solution(vector<int> &H) {
    if (H.size() == 1) return 1;
    int blocks = 0;
    int start = 0;
    vector<int>::iterator it = H.begin();
    stack<int> st;
    for(; it!=H.end(); it++) {
        if (st.size() && st.top() != *it) {
            if (st.top() > *it) {
                blocks++;
                start = *it;
                st.push(*it);
            }
            else {
                start += *it - st.top();
                st.push(*it);
            }
            if (st.top() == start) {
                ;
            }
        } else {
            if (!st.size()) {
                st.push(*it);
                blocks++;
            }
        }
    }
    return blocks;
}

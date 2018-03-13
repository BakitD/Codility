#include <string>
#include <stack>

int solution(string &S) {
    stack<char> st;
    for (string::iterator it = S.begin(); it!=S.end(); it++) {
        if (*it == '(') st.push(*it);
        else if (*it == ')') {
            if (!st.size()) return 0;
            else if (st.top() == '(') st.pop();
        }
    }
    return !st.size();
}

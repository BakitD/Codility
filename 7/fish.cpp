#include <stack>
#include <map>

using namespace std;

int solution(vector<int> &A, vector<int> &B) {
    int n = A.size();
    int alive = n;
    stack<int> st;
    for (int i = 0; i < n; i++) {
        if (B[i]) st.push(i);
        else if (st.size() && st.top() < i && !B[i]) {
            while (st.size() && A[st.top()] < A[i]) {
                st.pop();
                alive --;
            }
            if (st.size() && A[st.top()] > A[i]) alive--;
        }
    }
    return alive;
}

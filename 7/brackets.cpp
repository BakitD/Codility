#include <stack>
#include <string>

using namespace std;

int solution(string &S) {
    stack<char> st;
    string::iterator start = S.begin();
    string::iterator end = S.end();
    if (*start == '}' || *start == ']' || *start == ')' || *end == '{' || *end == '[' || *end == '(')
        return 0;
    if (S.substr(0,4) == "()()" || S.substr(0,4) == "[][]" || S.substr(0,4) == "{}{}") return 0;
    for (string::iterator c = start; c!=end; c++) {
        if (*c == '{' || *c == '[' || *c == '(') st.push(*c);
        else if (*c == '}' && st.top() == '{') st.pop();
        else if (*c == ')' && st.top() == '(') st.pop();
        else if (*c == ']' && st.top() == '[') st.pop();
    }
    return !st.size();
}

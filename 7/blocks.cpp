#include <stack>
#include <vector>

int solution(vector<int> &H) {
    int blocks = 0;
    stack<int> stack;

    for(vector<int>::iterator it = H.begin(); it!=H.end(); it++) {
        while(!stack.empty() && stack.top() > *it)
            stack.pop();
        if (!stack.empty() && stack.top() == *it)
            ;
        else {
            blocks++;
            stack.push(*it);
        }
    }
    return blocks;
}
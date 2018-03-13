#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>

using namespace std;

stack<int> leader(vector<int> &A) {
    stack<int> st;
    for (vector<int>::iterator it = A.begin(); it!=A.end(); it++) {
        if (!st.size() || st.top() == *it) st.push(*it);
        else if (st.size() && st.top() != *it) st.pop();
    }
    return st;
}

void pv(vector<int> &A) {
	for(vector<int>::iterator it = A.begin(); it!=A.end(); it++) cout << *it << "  ";
	cout << "\n";
}


int solution(vector<int> &A) {
    if (!A.size()) return 0;
    if (A.size() == 1) return 1;
    int equis = 0;


    for (vector<int>::iterator it = A.begin()+1; it!=A.end(); it++){
        vector<int> first = vector<int>(A.begin(), it);
        vector<int> second = vector<int>(it, A.end());

        stack<int> f = leader(first);
        stack<int> s = leader(second);

        if (f.size() && s.size() && f.top() == s.top()) {
            int nf = count(A.begin(), it, f.top());
            int ns = count(it, A.end(), s.top());
            if (first.size() - nf < nf && second.size() - ns < ns) equis++;
        }

        /*cout << "\n";
        pv(first);
        pv(second);
    	if (f.size() && s.size()) {
            	if (f.top() == s.top()) equis++;
    		cout << f.top() << " " << s.top() << "\n-------------------------\n";
    	}*/
    }
    return equis;
}


int main() {
	vector<int> v = {4,4,2,5,3,4,4,4};
	cout << solution(v);
}

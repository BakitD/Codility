#include <vector>
#include <iostream>
#include <stdlib.h>

using namespace std;

int solution(vector<int> &A) {
    const int v_size = A.size();
    int barrier_diff = 2 * 100000;
    int left = 0;
    int right = 0;
    int current = 0;
    for (int i = 0; i < v_size - 1; i++) {
    	left += A[i];
    	right = 0;
    	for (int j = i + 1; j < v_size; j++) right += A[j];
    	current = abs(left - right);
    	if (current < barrier_diff) barrier_diff = current;
    }
    return barrier_diff;
}


int main(int argc, char **argv)
{
	vector<int> tvector;
	tvector.push_back(3);
	tvector.push_back(5);
	std::cout << solution(tvector);
    return 0;
}

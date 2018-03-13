#include <iostream>
#include <math.h>


int solution(int x, int y, int d)
{
	if (y == x) return 0;
	if (y - x <= d) return 1;
	return ceil(((double)y - x) / (double)d);
}



int main()
{
	std::cout << solution(10, 85, 30);
}


class Point(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return '{},{}'.format(self.x, self.y)


def vecmult(a, b, c):
    return a.x*(b.y-c.y) - a.y*(b.x-c.x) + b.x*c.y - c.x*b.y


def solution(A):
    n = len(A)

    sign = vecmult(A[-1], A[0], A[1])
    for i in range(1, n-1):
        adjacent_sign = vecmult(A[i-1], A[i], A[i+1])
        if adjacent_sign * sign < 0:
            return i
        sign = adjacent_sign
    return -1


points = [Point(-1,3), Point(1,2), Point(3,1), Point(0,-1), Point(-2,1)]
solution(points)
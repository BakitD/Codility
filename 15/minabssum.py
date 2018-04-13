def solution(A):
    n = len(A)

    if n == 1:
        return abs(2*A[0])

    minimal = abs(A[0] + A[1])
    for i in range(0, n):
        for j in range(i, n):
            s = abs(A[i] + A[j])
            if s < minimal:
                minimal = s
    return minimal
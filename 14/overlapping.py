def solution(A, B):
    
    n = len(A)
    if n == 1: return 1

    maximal = 0
    for i in range(0, n):
        current = 0
        for j in range(0, n):
            if i < j and B[i] < A[j]: current += 1
            elif i > j and A[i] > B[j]: current += 1
        if maximal < current:
            maximal = current
    return maximal


solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10])
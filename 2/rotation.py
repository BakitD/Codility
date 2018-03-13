def solution(A, K):
    n = len(A)
    result = [0] * n
    if K in [0, n]: return A

    for i in range(0, n): result[(i + K) % n] = A[i]
    return result

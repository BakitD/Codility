def solution(K, A):
    n = len(A)
    
    if n == 1 and A[0] >= K: return 1
    
    temp = 0
    result = 0
    for i in range(n):
        temp += A[i]
        if temp >= K:
            result += 1
            temp = 0
    return results
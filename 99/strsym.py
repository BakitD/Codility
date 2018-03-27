def solution(S):
    n = len(S)
    if n == 1: return 0
    if n == 2: return -1
    if n == 3 and S[0] != S[2]: return -1
    if n % 2 == 0: return -1

    for i in range(n):
        if S[i] != S[n-i-1]: return -1
    return n // 2


print(solution('racecar'), 3)
print(solution('barakarab'), 4)
print(solution('x', 0))
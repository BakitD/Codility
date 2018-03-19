def solution(A):
    if len(A) == 2: return abs(A[1] - A[0])

    n = len(A)
    sums = [A[0],]
    rev_sums = [A[n-1],]
    for i in range(1, n-1):
        sums.append(sums[i-1] + A[i])
        rev_sums.append(rev_sums[i-1] + A[n - i - 1])
    minimal = 1000 * n
    ln = len(sums)
    for i in range(0, ln):
        diff = abs(sums[i] - rev_sums[ln - i - 1])
        if diff < minimal:
            minimal = diff
    return minimal

print(solution([-10, -20, -30, -40, 100]))
print(solution([3,1,2,4,3]))

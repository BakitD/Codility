
def solution(A):
    d = {}
    n = len(A)
    results = [0] * n

    for i in range(n):
        if A[i] in d:
            results[i] = d[A[i]]
            continue
        for j in range(n):
            if A[i] % A[j] != 0 and i != j:
                if not A[i] in d: d[A[i]] = 1
                else: d[A[i]] += 1
        results[i] = d[A[i]] if A[i] in d else 0
    return results
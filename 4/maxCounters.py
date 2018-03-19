def solution(N, A):
    n = len(A)
    counter = 0
    max_counter = 0
    d = {}
    barrier = 0

    for i in range(0, n):
        if A[i] == N + 1:
            counter = max_counter
            barrier = max_counter
            d = {}
        else:
            if not A[i] in d: d[A[i]] = 1
            else: d[A[i]] += 1
            if d[A[i]] + barrier > max_counter:
                max_counter = d[A[i]] + barrier
    vector = [counter] * N
    for key, value in d.items():
        vector[key-1] += value
    return vector
            

solution(5, [3, 4, 4, 6, 1, 4, 4])
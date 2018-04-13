def solution(M, A):
    if M <= 1:
        return M
    n = len(A)
    if n <= 0:
        return n

    slices = list(set(A) - set([A[0]])) + [set([A[0]]),]
    slc = slices[-1]
    i = 1
    j = 0
    while i < n:
        if A[i] in slc:
            slices.append(slc)
            i = j
            j += 1
        else:
            slc.add(A[i])
            i += 1
    return len(slices)


solution(6, [3, 4, 5, 5, 2])
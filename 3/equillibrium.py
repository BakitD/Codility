def solution(A):
    minimal = sum(A)
    minIndex = 1
    for index in range(1, len(A)):
        minT = abs(sum(A[:index]) - sum(A[index:]))
        if minT < minimal:
            minIndex = index
    return minIndex


solution([3,1,2,4,3])

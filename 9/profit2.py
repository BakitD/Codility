
def solution(A):
    if len(A) == 0: return 0;
    if len(A) == 2: return A[1] - A[0] if A[1] - A[0] > 0 else 0

    minIndex = 0
    maxIndex = 1
    minimal = A[minIndex]
    maximal = A[maxIndex]
    current = maximal - minimal
    profit = 0
    for i in range(0, len(A)-1):
        if maximal - A[i] > current and i < maxIndex:
            minimal = A[i]
            minIndex = i
        if A[i+1] - minimal > current:
            maximal = A[i+1]
            maxIndex = i+1
        if A[i+1] - A[i] > current and A[i+1] - A[i] > maximal - minimal:
            maxIndex = i + 1
            minIndex = i
            maximal = A[maxIndex]
            minimal = A[minIndex]
        current = maximal - minimal
    for i in range(maxIndex, 0, -1):
        if maximal - A[i] > current:
            current = maximal - A[i]
    return current if current > 0 else 0

#solution(  [23171, 21011, 21123, 21366, 21013, 21367] )
solution([99,3,4,2,1,2,3,5,1])



def solution(A):
    peaks = []
    stack = []
    peakNumber = 0
    for index in range(1, len(A)-1):
        if A[index-1] < A[index] > A[index+1]:
            peaks.append(index)
    for p in peaks:
        if not stack:
            stack.append(p)
        elif abs(p - stack[-1]) >= len(peaks):
            stack.append(p)
    return len(stack)


solution([1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2])

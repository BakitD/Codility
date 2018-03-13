def solution(A):
    if len(A) == 1: return A[0]
    max_slice = max_ending = 0
    all_negative = True
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_ending, max_slice)
        if a > 0: all_negative = False
    return max(A) if all_negative else max_slice

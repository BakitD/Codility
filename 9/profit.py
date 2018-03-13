def solution(A):
    profit = 0
    for i in range(0, len(A)-1):
        diff = max(A[i+1:]) - A[i]
        profit = diff if diff > profit else profit
    return profit

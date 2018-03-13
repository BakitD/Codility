def solution(A):
    n = len(A)
    if n < 2: return 0
    if n == 2: return A[1] - A[0] if A[1] > A[0] else 0

    maxI = minI = 0
    profit = 0
    for i in range(0, n-1):
        if A[i+1] - A[i] > profit:
            maxI = i + 1
            minI = i
            profit = A[i+1] - A[i]
        elif A[i+1] - A[minI] > profit:
            maxI = i + 1
            profit = A[i+1] - A[minI]
        elif A[maxI] - A[i] > profit and maxI > i:
            minI = i
            profit = A[maxI] - A[i]
    if n-1 == maxI:
        diff = A[maxI] - min(A[:-1])
        profit = profit if profit > diff else diff
    return profit if profit > 0 else 0


def main():
  solution([1,2,3,100,20])

main()

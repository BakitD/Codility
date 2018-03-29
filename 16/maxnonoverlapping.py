def solution(A, B):
    n = len(A)
    if n == 0:
        return 0

    counter = 1
    last = B[0]
    for i in range(1, n):
        if A[i] > last:
            last = B[i]
            counter += 1
    return counter


print(solution([],[]), 0)
print(solution([1,6,12,18,24],[4,8,14,20,28]), 5)
print(solution([1, 3, 7, 9, 9], [5, 6, 8, 9, 10]), 3)
print(solution([0, 2, 100], [0, 50, 1000]), 3)
print(solution([0,3,8,15,21,27], [6,12,18,24,30,33]), 3)
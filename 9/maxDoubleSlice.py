ef solution(A):

    n = len(A)
    if n == 4:
        return A[1] + A[2]

    fmax = 0
    bmax = 0
    pref = [A[0],] + [0] * (n-1)
    post = [A[n-1],] + [0] * (n-1)

    for i in range(1, n):
        pref[i] = A[i] + pref[i-1]
        post[i] = A[n-i-1] + post[i-1]

    maximal = right = left = 0
    index = 0
    for i in range(1, n-1):
        if pref[i] <= pref[i-1] and pref[i] <= pref[i+1]:
            j = i - 1
            left = right = 0
            while j >= 0 and pref[j-1] <= pref[j]:
                left += A[j]
                j -= 1
            j = n - i - 2
            while j >= 0 and post[j-1] <= post[j]:
                right += A[n-j-1]
                j -= 1
        if right + left > maximal:
            maximal = left + right
            index = i
    return maximal

print(solution([0, 10, -5, -2, 0]), 10)
print(solution([5, 0, 1, 0, 5]), 1)
print(solution([3, 2, 6, -1, 4, 5, -1, 2]), 17)
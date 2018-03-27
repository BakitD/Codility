def sieve(n):
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    i = 2
    while i*i <= n:
        if sieve[i]:
            k = i * i
            while k <= n:
                sieve[k] = False
                k += i
        i += 1
    return sieve


def isSemiprime(n, es):
    i = 2
    while(i * i <= n):
        k = n // i
        if not n % i and es[i] and (i == k or es[k]):
            return True
        i += 1
    return False


def solution(N, P, Q):
    k = len(P)
    result = [0] * k
    semiprimes = [0] * (N+1)
    semiprimes_pos = [0] * (N+1)
    es = sieve(N)

    for i in range(4, N+1):
        if not es[i] and isSemiprime(i, es):
            semiprimes[i] = semiprimes[i-1] + 1
            semiprimes_pos[i] = 1
        else:
            semiprimes[i] = semiprimes[i-1]

    for i in range(0, k):
        result[i] = semiprimes[Q[i]] - semiprimes[P[i]] + semiprimes_pos[P[i]]

    return result


print(solution(26, [1, 4, 16], [26, 10, 20]), '')
#print(solution(6, [0,0,1,1,1,2],[1,0,5,6,2,2]))
#print(solution(20, [15],[20]))


#print(solution(187, [1, 4, 16], [26, 10, 20]))
#print(solution(6, [0,0,2,4,4], [0,1,5,6,4]))
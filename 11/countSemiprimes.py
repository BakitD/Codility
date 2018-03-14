def primaliry(n):
    i = 2
    while (i*i <= n):
        if n % i == 0:
            return False
        i += 1
    return True

def isSemiprime(n):
    i = 2
    while(i * i <= n):
        if not n % i:
            if primaliry(i):
                k = n // i
                if i == k or primaliry(n // i):
                    return True
        i += 1
    return False


def solution(N, P, Q):
    result = []
    semiprimes = []
    positions = {0:0, 1:0, 2:0, 3:0, 4:0}

    for x in range(4, N+1):
        if isSemiprime(x):
            semiprimes.append(x)

    last = 1
    for i in range(5, N+1):
        if i in semiprimes:
            positions[i] = last
            last += 1
        else:
            positions[i] = last

    #for k,v in positions.items(): print(k,v)
    for p,q in zip(P,Q):
        result.append(positions[q] - positions[p])
        if q in semiprimes: result[-1] += 1
    return result



print(solution(26, [1, 4, 16], [26, 10, 20]), '')
#print(solution(6, [0,0,1,1,1,2],[1,0,5,6,2,2]))
print(solution(20, [15],[20]))


#print(solution(187, [1, 4, 16], [26, 10, 20]))
#print(solution(6, [0,0,2,4,4], [0,1,5,6,4]))

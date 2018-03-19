def solution(A):
    n = len(A)

    if n == 1: return 0;
    if n == 2: return int(A[0] == A[1])
    if len(set(A)) == len(A): return 0

    st = {x: 0 for x in range(0, 10)}
    rst = {x: 0 for x in range(0, 10)}
    equis = [A[0],] + [None] * (n - 1)
    requis = [A[n-1],] + [None] * (n - 1)
    st[A[0]] = 1
    rst[A[n-1]] = 1
    smax = [0,1]
    rsmax = [A[n-1],1]

    for i in range(1, n):
        half = (i+1)//2
        if not A[i] in st: st[A[i]] = 1
        else: st[A[i]] += 1
        if st[A[i]] > smax[1]:
            smax[1] = st[A[i]]
            smax[0] = A[i]
        if st[smax[0]] > half: equis[i] = smax[0]
       
        if not A[n-i-1] in rst: rst[A[n-i-1]] = 1
        else: rst[A[n-i-1]] += 1
        if rst[A[n-i-1]] > rsmax[1]:
            rsmax[1] = rst[A[n-i-1]]
            rsmax[0] = A[n-i-1]
        if rst[rsmax[0]] > half: requis[i] = rsmax[0]

    equi_leaders = 0
    for i in range(0, n-1):
        if equis[i] == requis[n - 2 - i]:
            equi_leaders += 1
    return equi_leaders

    
print(solution([4,3,4,4,4,2]))
print(solution([0,0]))
print(solution([0,0,5]))
print(solution([0,0,0]))
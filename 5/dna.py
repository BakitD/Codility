def solution(S, P, Q):
    n = len(S)
    m = len(P)
    d = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    if n == 1: return [d[S[0]]] 

    ent = [{1: 0, 2: 0, 3: 0, 4: 0}] * (n + 1)
    for i in range(1, n+1):
        ent[i] = dict(ent[i-1])
        ent[i][d[S[i-1]]] += 1

    results = [0] * m
    for i in range(0, m):
        if P[i] == Q[i]:
            results[i] = d[S[P[i]]]
        elif d[S[P[i]]] == 1 or d[S[Q[i]]] == 1:
            results[i] = 1
        elif Q[i] - P[i] <= 2:
            results[i] = d[S[P[i]]] if d[S[P[i]]] < d[S[Q[i]]] else d[S[Q[i]]]
        else:
            left = P[i] + 1
            right = Q[i] + 1
            if ent[right][1] - ent[left][1] > 0: results[i] = 1
            elif ent[right][2] - ent[left][2] > 0: results[i] = 2
            elif ent[right][3] - ent[left][3] > 0: results[i] = 3
            else: results[i] = 4
            
            
    return results

print(solution('GT', [0, 0, 1], [0, 1, 1]) , '[3,3,4]')
#solution('CAGCCTA', [2, 5, 0], [4, 5, 6])
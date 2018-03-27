def solution(P, C):
    p = (P - 1 if P % 2 else P) // 2
    return C if p >= C else p
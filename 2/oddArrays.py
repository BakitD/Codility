def solution(A):
    bin = set()
    for e in A:
        if not e in bin: bin.update([e])
        elif e in bin: bin.remove(e)
    return list(bin)[0]

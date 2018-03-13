def solution(A):
    counters = {}
    half = len(A) / 2
    index = 0
    for element in A:
        if element in counters.keys():
            counters[element] += 1
        else:
            counters[element] = 1
        if counters[element] > half: return index
        index += 1
    return -1

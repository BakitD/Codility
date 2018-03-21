def solution(S):
    words = S.split()
    maximal = 0
    numbers = [x for x in range(0,10)]
    for word in words:
        n = 0
        if len(word) % 2 != 0:
            for symbol in word:
                n += symbol in numbers
        maximal = n if n % 2 == 0 and n > maximal else maximal
                
    return maximal
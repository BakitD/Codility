def primarily(n):
    i = 2
    while(i * i <= n):
        if n % i == 0:
            return False
        i += 1
    return True

def solution(A, B):
    total = 0
    for a, b in zip(A, B):
        if a == b:
            total += 1
            continue
        if a < 5 and b < 5 and a != b:
            continue
        if a != b and primarily(a) and primarily(b):
            continue

        i = 2
        first = set()
        second = set()
        maxOf = max(a, b)

        while (i * i <= maxOf):
            if primarily(i):
                if i <= a and a % i == 0:
                    first.add(i)
                if i <= b and b % i == 0:
                    second.add(i)
            i += 1
        #if a % b == 0: first.add(b)
        #if b % a == 0: second.add(a)

        if  len(first) and len(second) and len(first - second) == 0 and len(second - first) == 0:
            total += 1

    return total


print('>>>', solution([3, 9, 20, 11], [9, 81, 5, 13]), 2)
print('>>>', solution([15, 10, 9], [75, 30, 5]), 1)
print('>>>', solution([6059, 551], [442307, 303601]), 2)
print('>>>', solution([7, 17, 5, 3], [7, 11, 5, 2]), 2)


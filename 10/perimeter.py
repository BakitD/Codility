def solution(N):
    i = 1
    minimal = N + 1
    while (i * i <= N):
        if (N % i == 0):
            d = i + N // i
            if d < minimal:
                minimal = d
        i += 1
    return minimal + minimal


def main():
    assert(solution(101)==204)

main()

def solution(S):
    numbers = set([str(x) for x in range(10)])
    chars = set([chr(x) for x in range(ord('A'), ord('Z'))] + [chr(x) for x in range(ord('a'), ord('z'))] + ['z', 'Z'])

    words = S.split()
    maximal = ''

    for word in words:
        word_len = len(word)
        if word_len % 2 == 0:
            continue
        nums = 0
        chrs = 0
        for letter in word:
            if letter in numbers: nums += 1
            elif letter in chars: chrs += 1
            else: continue
        if chrs % 2 == 0 and nums % 2 != 0 and chrs + nums == word_len and word_len > len(maximal):
            maximal = word
    return len(maximal) if len(maximal) else -1


print(solution('0'), 1)
print(solution('a'), -1)
print(solution('zaq123edc'), 9)
print(solution('test 5 a0A pass007 ?xy1'), 7)
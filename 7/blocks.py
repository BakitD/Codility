
def solution(H):
    stack = []
    blocks = 0

    for height in H:
        while len(stack) and stack[-1] > height:
            stack.pop()
        if len(stack) and stack[-1] == height:
            pass
        else:
            blocks += 1
            stack.append(height)
    return blocks
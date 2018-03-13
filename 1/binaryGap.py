

def solution(N):
    mask = 1
    maximal = 0
    current = 0
    shifted = N
    i = 0
    started = False
    while(i < len(bin(N))):
        value = (shifted >> i) & mask
        i += 1
        if value:
            if (current > maximal and i < N): 
                maximal = current
            current = 0
            started = True
        elif started:
            current += 1
    return maximal


print(solution(1376796946))
              
        
            

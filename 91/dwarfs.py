

def occupy(parts, coordinates, numberBorder, letterBorder, dwarfs=False):
    for coordinate in coordinates:
        if coordinate[0] < numberBorder and coordinate[1] < letterBorder:
            parts[0][1] -= 1
            parts[0][2] += dwarfs
        if coordinate[0] >= numberBorder and coordinate[1] < letterBorder:
            parts[2][1] -= 1
            parts[2][2] += dwarfs
        if coordinate[0] < numberBorder and coordinate[1] >= letterBorder:
            parts[1][1] -= 1
            parts[1][2] += dwarfs
        if coordinate[0] >= numberBorder and coordinate[1] >= letterBorder:
            parts[3][1] -= 1
            parts[3][2] += dwarfs
    return parts


def solution(N, S, T):
    free = (N/2) * (N/2)
    parts = [['lf', free, 0], ['rf', free, 0], ['lb', free, 0], ['rb', free, 0]]
    letters = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    lb = letters[N//2]
    nb = str(N // 2 + 1)

    barrels = S.split()
    occupied = T.split()
    parts = occupy(occupy(parts, S.split(), nb, lb), T.split(), nb, lb, True)

    seats_limit = sorted(parts, key=lambda x: x[1])




    while True:
        for part in parts:
            if part[1]


solution(4, '1B 1C 4B 1D 2A', '3B 2D')
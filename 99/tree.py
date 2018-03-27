class Tree:
    def __init__(self, x):
        self.x = x
        self.r = None
        self.l = None

    def __str__(self):
        return '{}'.format(self.x)

    def build(tree):
        t = Tree(tree[0])
        if tree[1]:
            t.l = Tree.build(tree[1])
        if tree[2]:
            t.r = Tree.build(tree[2])
        return t


def dive(node, level, max_level):
    if node.l == None and node.r == None:
        if level > max_level[0]:
            max_level[0] = level
        return level - 1
    if node.l:
        level = dive(node.l, level+1, max_level)
    if node.r:
        level = dive(node.r, level+1, max_level)
    return level - 1



def solution(T):
    max_depth = [0]
    dive(T, 0, max_depth)
    return max_depth[0]


print(solution(Tree.build(
    (5,
        (3, 
            (20, None, None),
            (21, (22, None, None), None)),
        (10, 
            (1, None, None), None)
        )
    )
))



'''Codility decision
from extratypes import Tree  # library with types used in the task

def dive(node, level, max_level):
    if node.l == None and node.r == None:
        if level > max_level[0]:
            max_level[0] = level
        return level - 1
    if node.l:
        level = dive(node.l, level+1, max_level)
    if node.r:
        level = dive(node.r, level+1, max_level)
    return level - 1



def solution(T):
    max_depth = [0]
    dive(T, 0, max_depth)
    return max_depth[0]
'''
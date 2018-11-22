from test_framework import generic_test
from collections import deque

def binary_tree_depth_order(tree):
    q = deque()
    q.append((1,tree))
    res = []
    while q:
        depth, curr = q.pop()
        if not curr:
            continue
        q.appendleft((depth + 1, curr.left))
        q.appendleft((depth + 1, curr.right))

        if not res or res[-1][-1][0] < depth:
            res.append([(depth, curr.data)])
        else:
            res[-1].append((depth, curr.data))
    return [[x[1] for x in l] for l in res]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))

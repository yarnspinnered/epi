from test_framework import generic_test
from collections import namedtuple

node = namedtuple("node", ["height", "balanced"])
def is_balanced_binary_tree(u):
    def helper(tree):
        if not tree:
            return node(0, True)
        l_height, l_bal = helper(tree.left)
        r_height, r_bal = helper(tree.right)
        if abs(l_height - r_height) > 1 or not l_bal or not r_bal:
            return node(0, False)
        return  node(max(l_height, r_height) + 1, True)
    return helper(u).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))

from test_framework import generic_test
from collections import namedtuple

def is_balanced_binary_tree(tree):
    node = namedtuple("node", ["height", "balanced"])
    if not tree:
        return True
    def helper(u):
        if not u:
            return node(0, True)
        else:
            left_info = helper(u.left)
            right_info = helper(u.right)
            height = max(left_info.height, right_info.height) + 1
            if not left_info.balanced or not right_info.balanced or abs(left_info.height - right_info.height) > 1:
                return node(height, False)
            else:
                return node(height, True)


    return helper(tree).balanced


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_balanced.py",
                                       'is_tree_balanced.tsv',
                                       is_balanced_binary_tree))

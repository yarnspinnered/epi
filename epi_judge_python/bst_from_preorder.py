from test_framework import generic_test
from bst_node import BstNode

def rebuild_bst_from_preorder(preorder_sequence):

    i =0
    def rebuild_within_range(low=float('-inf'), high=float('inf')):
        nonlocal i
        if i >= len(preorder_sequence):
            return None
        v = preorder_sequence[i]
        if low <= v <= high:
            u = BstNode(v)
            i += 1
            u.left = rebuild_within_range(low=low, high=v)
            u.right = rebuild_within_range(low=v, high=high)

            return u
        return None

    res = rebuild_within_range()
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("bst_from_preorder.py",
                                       'bst_from_preorder.tsv',
                                       rebuild_bst_from_preorder))

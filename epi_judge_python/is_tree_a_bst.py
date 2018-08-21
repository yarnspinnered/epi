from test_framework import generic_test


def is_binary_tree_bst(tree, low_range=float('-inf'), high_range=float('inf')):
    def helper(tree):
        if not tree:
            return True, high_range, low_range
        left_status, left_small, left_big = helper(tree.left)
        right_status, right_small, right_big = helper(tree.right)
        status = tree.data >= left_big and tree.data <= right_small and left_status and right_status
        small = min(tree.data, left_small, right_small)
        big = max(tree.data, left_big, right_big)
        return status, small, big

    return helper(tree)[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_a_bst.py", 'is_tree_a_bst.tsv',
                                       is_binary_tree_bst))

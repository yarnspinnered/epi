from test_framework import generic_test
from binary_tree_node import BinaryTreeNode

def binary_tree_from_preorder_inorder(preorder, inorder):
    inorder_map = {v : i for i,v in enumerate(inorder)}
    def helper(pre_start, pre_end, in_start, in_end):
        if pre_start >= pre_end or in_start >= in_end:
            return None
        middle_of_inorder = inorder_map[preorder[pre_start]]
        left_size = middle_of_inorder - in_start
        root = BinaryTreeNode(preorder[pre_start],
                              helper(pre_start + 1,
                                     pre_start + 1 + left_size,
                                     in_start,
                                     in_start + left_size),
                              helper(pre_start + 1 + left_size,
                                     pre_end,
                                     inorder.index(preorder[pre_start]) + 1,
                                     in_end))
        return root

    return helper(0, len(preorder), 0, len(inorder))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_from_preorder_inorder.py",
                                       'tree_from_preorder_inorder.tsv',
                                       binary_tree_from_preorder_inorder))

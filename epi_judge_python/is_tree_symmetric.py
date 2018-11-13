from test_framework import generic_test


def is_symmetric(tree):
    def helper(l,r):
        if l == r:
            return True
        elif l == None or r == None:
            return False
        elif l.data != r.data:
            return False
        else:
            return helper(l.left, r.right) and helper(l.right, r.left)
    return tree is None or helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))

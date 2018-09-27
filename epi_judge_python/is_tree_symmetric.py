from test_framework import generic_test


def is_symmetric(tree):
    def helper(l,r):
        if not l and not r:
            return True
        elif l and r:
            return l.data == r.data and helper(l.left,r.right) and helper(l.right, r.left)
        else:
            return False

    return not tree or helper(tree.left, tree.right)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))

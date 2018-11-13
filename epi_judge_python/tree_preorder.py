from test_framework import generic_test


def preorder_traversal(tree):
    if not tree:
        return []
    stack = [tree]

    res = []
    while stack:
        c = stack.pop()
        res.append(c.data)
        if not c.right is None:
            stack.append(c.right)
        if not c.left is None:
            stack.append(c.left)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_preorder.py", 'tree_preorder.tsv',
                                       preorder_traversal))

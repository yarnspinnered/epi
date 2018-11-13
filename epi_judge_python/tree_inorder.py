from test_framework import generic_test


def inorder_traversal(tree):
    if not tree:
        return []
    stack, u= [], tree

    while u is not None:
        stack.append(u)
        u = u.left

    res = []
    while stack:
        c = stack.pop()
        res.append(c.data)
        c_right = c.right
        while c_right is not None:
            stack.append(c_right)
            c_right = c_right.left


    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_inorder.py", 'tree_inorder.tsv',
                                       inorder_traversal))

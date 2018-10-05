from test_framework import generic_test


def inorder_traversal(tree):
    if not tree:
        return []
    res = []
    prev = None

    while tree:
        new_prev = tree
        if prev is tree.parent:
            if tree.left:
                tree = tree.left
            elif tree.right:
                res.append(tree.data)
                tree = tree.right
            else:
                res.append(tree.data)
                tree = tree.parent
        elif prev is tree.left:
            res.append(tree.data)
            if tree.right:
                tree = tree.right
            else:
                tree = tree.parent
        else:
            tree = tree.parent

        prev = new_prev

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))

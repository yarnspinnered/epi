from test_framework import generic_test


def is_symmetric(tree):
    def check_symmetric(node_1, node_2):
        if not node_1 and not node_2:
            return True
        elif node_1 and node_2:
            return node_1.data == node_2.data and check_symmetric(node_1.left, node_2.right) and check_symmetric(node_1.right, node_2.left)
        else:
            return False

    if not tree:
        return True
    else:
        return check_symmetric(tree.left, tree.right)



if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_tree_symmetric.py",
                                       'is_tree_symmetric.tsv', is_symmetric))

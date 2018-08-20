from test_framework import generic_test


# We use stack and previous node pointer to simulate postorder traversal.
def postorder_traversal(tree):
    if not tree:
        return []
    def inverse_postorder(root):

        res, stack = [], [root]

        while stack:
            curr = stack.pop()
            res.append(curr.data)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return res

    return inverse_postorder(tree)[::-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "tree_postorder.py", 'tree_postorder.tsv', postorder_traversal))

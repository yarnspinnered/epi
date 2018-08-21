from test_framework import generic_test


# We use stack and previous node pointer to simulate postorder traversal.
def postorder_traversal(tree):
    # if not tree:
    #     return []
    # def inverse_postorder(root):
    #
    #     res, stack = [], [root]
    #
    #     while stack:
    #         curr = stack.pop()
    #         res.append(curr.data)
    #         if curr.left:
    #             stack.append(curr.left)
    #         if curr.right:
    #             stack.append(curr.right)
    #     return res
    # return inverse_postorder(tree)[::-1]
    if not tree:
        return []

    stack, res, prev = [tree], [], None

    while stack:
        curr = stack[-1]
        if not prev or curr is prev.left or curr is prev.right:
            if curr.left:
                stack.append(curr.left)
            elif curr.right:
                stack.append(curr.right)
            else:
                res.append(curr.data)
                stack.pop()
        elif curr.left is prev:
            if curr.right:
                stack.append(curr.right)
            else:
                res.append(curr.data)
                stack.pop()
        else:
            res.append(curr.data)
            stack.pop()

        prev = curr
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "tree_postorder.py", 'tree_postorder.tsv', postorder_traversal))

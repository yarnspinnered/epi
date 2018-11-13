from test_framework import generic_test, test_utils


def find_k_largest_in_bst(tree, k):
    res = []
    def helper(u):
        if u:
            helper(u.right)
            if len(res) < k:
                res.append(u.data)
                helper(u.left)
    helper(tree)
    return res[-k:]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "k_largest_values_in_bst.py", 'k_largest_values_in_bst.tsv',
            find_k_largest_in_bst, test_utils.unordered_compare))

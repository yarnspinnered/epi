from test_framework import generic_test, test_utils


def generate_balanced_parentheses(n):
    def helper(state, left_needed, right_needed):
        if left_needed > 0:
            helper( state + "(", left_needed - 1, right_needed)
        if left_needed < right_needed:
            helper(state + ")", left_needed, right_needed - 1)
        if right_needed == 0:
            res.append(state)
            return
    res = []
    helper("", n , n)
    return res
if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))

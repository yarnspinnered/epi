from test_framework import generic_test, test_utils


def combinations(n, k):
    def helper(offset, state):
        if len(state) == k:
            res.append(list(state))
            return
        i = offset
        while i <= n:
            helper(i + 1, state + [i])
            i += 1


    res = []
    helper(1, [])
    return res

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))

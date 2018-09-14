from test_framework import generic_test, test_utils


def generate_power_set(S):
    def helper(S):
        if len(S) == 0:
            return [[]]
        res = []
        prev = helper(S[:-1])
        for e in prev:
            res.append(e + [S[-1]])

        return (prev + res)

    return helper(S)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))

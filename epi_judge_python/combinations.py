from test_framework import generic_test, test_utils


def combinations(n, k):
    # TODO - you fill in here.
    def helper(offset, some):
        if some == 0:
            return [[]]
        if  some == offset:
            return [[x for x in range(1, offset + 1)]]
        res = []

        with_last = helper(offset - 1, some - 1)
        for e in with_last:
            res.append(e + [offset])
        without_last = helper(offset - 1, some)
        res.extend(without_last)

        return res
    return helper(n, k)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))

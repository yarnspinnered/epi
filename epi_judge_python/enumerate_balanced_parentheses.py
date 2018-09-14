from test_framework import generic_test, test_utils


def generate_balanced_parentheses(n):
    cache = {0 : [""]}
    def helper(num_pairs):
        if num_pairs in cache:
            return cache[num_pairs]
        res = ['(' + x + ')' for x in helper(num_pairs - 1)]

        for i in range(1, num_pairs):
            join_left = helper(i)
            join_right = helper(num_pairs - i)
            res.extend([x + y for x in join_left for y in join_right])
        cache[num_pairs] =list(set(res))
        return cache[num_pairs]

    return helper(n)

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))

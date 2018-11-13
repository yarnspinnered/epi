from test_framework import generic_test


def compute_binomial_coefficient(n, k):
    if k > n:
        return 0
    if k == n:
        return 1
    cache = [0 for j in range(k + 1)]
    cache[0] = 1

    for i in range(1, n + 1):
        # print("before", cache)
        new_cache = [0 for _ in range(k + 1)]
        new_cache[0] = 1

        for j in range(1, k + 1):
            new_cache[j] = cache[j] + cache[j - 1]
        cache = new_cache
        # print("after: ", cache)
    return cache[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))

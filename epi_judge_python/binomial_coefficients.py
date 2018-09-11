from test_framework import generic_test


def compute_binomial_coefficient(n, k):
    cache = [[0 for j in range(k + 1)] for i in range(n + 1 )]
    for i in range(n + 1):
        cache[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, min(k + 1, i + 1)):
            cache[i][j] = cache[i - 1][j - 1] + cache[i - 1][j]

    return cache[n][k]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))

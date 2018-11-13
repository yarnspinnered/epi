from test_framework import generic_test


def number_of_ways(n, m):

    cache = [[0 for _ in range(m)] for _ in range(n)]
    cache[0] = [1 for _ in range(m)]
    for i in range(n):
        cache[i][0] = 1

    for i in range(1, n):
        for j in range(1,m):
            cache[i][j] = cache[i - 1][j] + cache[i][j - 1]

    return cache[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))

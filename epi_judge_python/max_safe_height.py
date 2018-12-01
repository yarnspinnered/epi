from test_framework import generic_test


def get_height(cases, drops):
    F = [[0 for _ in range(cases + 1)] for _ in range(drops + 1)]
    if cases == 0 or drops == 0:
        return 0
    for i in range(drops + 1):
        F[i][1] = i
    for j in range(2, cases + 1):
        for i in range(1, drops + 1):
            F[i][j] = F[i - 1][j] + 1 + F[i - 1][j - 1]


    return F[drops][cases]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_safe_height.py",
                                       'max_safe_height.tsv', get_height))

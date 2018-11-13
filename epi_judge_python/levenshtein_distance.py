from test_framework import generic_test


def levenshtein_distance(A, B):
    cache = [[0 for _ in range(len(A) + 1)] for _ in range(len(B) + 1)]

    for i in range(len(B) + 1):
        cache[i][0] = i

    for j in range(len(A) + 1):
        cache[0][j] = j

    for i in range(1, len(B ) + 1):
        for j in range(1, len(A) + 1):
            if A[j - 1] == B[i - 1]:
                cache[i][j] = cache[i - 1][j - 1]
            else:
                cache[i][j] = min(
                    cache[i - 1][j],
                    cache[i - 1][j - 1],
                    cache[i][j - 1]
                ) + 1

    return cache[len(B)][len(A)]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))

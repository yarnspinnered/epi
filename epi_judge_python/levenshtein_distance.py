from test_framework import generic_test


def levenshtein_distance(A, B):
    cache = [[float('inf') for j in range(len(B) + 1)] for i in range(len(A) + 1)]
    cache[0] = [x for x in range(len(B) + 1)]
    for i in range(len(cache)):
        cache[i][0] = i

    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            up = cache[i - 1][j]
            left = cache[i][j - 1]
            diag = cache[i - 1][j - 1]
            if A[i - 1] == B[j - 1]:
                cache[i][j] = diag
            else:
                cache[i][j] = 1 + min(up, left, diag)
    return cache[len(A)][len(B)]
    return 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))

from test_framework import generic_test, test_utils
import itertools

def permutations(A):
    if len(A) == 0:
        return A
    elif len(A) == 1:
        return [A]

    res = []

    for perm in permutations(A[:-1]):
        for i in range(len(perm) + 1):
            new_perm = perm[:]
            new_perm.insert(i, A[-1])
            res.append(new_perm)
    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))

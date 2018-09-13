from test_framework import generic_test, test_utils


def permutations(A):
    if len(A) == 1:
        return [A]

    res = []
    last = A[-1]
    other_perms = permutations(A[:-1])
    for perm in other_perms:
        for j in range(len(perm) + 1):
            to_add = perm[:]
            to_add.insert(j, last)
            res.append(to_add)

    return res


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))

from test_framework import generic_test


def apply_permutation(perm, A):
    visited = [False for _ in range(len(A))]

    for i in range(len(A)):
        prev = None
        j = i

        while perm[j] >= 0:
            temp = perm[j]
            if not prev is None:
                prev, A[j] = A[j], prev

                perm[j] = perm[j] - len(perm)

            else:
                prev = A[j]

            j = temp

    return A


def apply_permutation_wrapper(perm, A):
    apply_permutation(perm, A)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("apply_permutation.py",
                                       "apply_permutation.tsv",
                                       apply_permutation_wrapper))

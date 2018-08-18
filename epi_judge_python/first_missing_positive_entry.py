from test_framework import generic_test


def find_first_missing_positive(A):
    i = 0
    if not A:
        return 1
    while i < len(A):
        x = A[i]
        if x < 0 or x >= len(A):
            i += 1
        elif x - 1== i:
            i += 1
        else:
            if A[x - 1] != x:
                A[x - 1], A[i] = A[i], A[x - 1]
            else:
                i += 1


    for i,x in enumerate(A):
        if i != x - 1:
            return i + 1

    return len(A) + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("first_missing_positive_entry.py",
                                       'first_missing_positive_entry.tsv',
                                       find_first_missing_positive))

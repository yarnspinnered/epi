from test_framework import generic_test


def find_first_missing_positive(A):
    def check(arr, idx):
        return arr[idx] == idx + 1
    i = 0
    while i < len(A):
        v = A[i]
        if v > 0 and v <= len(A):
            if not check(A, v -1):
                A[i], A[v - 1] = A[v - 1], A[i]
                continue
        i += 1

    for i,v in enumerate(A):
        if not check(A, i):
            return i + 1

    return len(A) + 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("first_missing_positive_entry.py",
                                       'first_missing_positive_entry.tsv',
                                       find_first_missing_positive))

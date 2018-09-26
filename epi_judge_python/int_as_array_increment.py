from test_framework import generic_test


def plus_one(A):
    for i in reversed(range(len(A))):
        A[i] += 1
        if A[i] <= 9:
            break
        else:
            A[i] = 0
    if A[0] == 0:
        A[0] = 0
        A.insert(0, 1)
    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_increment.py",
                                       "int_as_array_increment.tsv", plus_one))

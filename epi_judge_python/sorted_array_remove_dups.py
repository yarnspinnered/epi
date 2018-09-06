import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Returns the number of valid entries after deletion.
def delete_duplicates(A):
    unique = 0
    processing = 0
    while processing < len(A):
        if processing == 0:
            unique += 1
        else:
            if A[processing] == A[unique - 1]:
                pass
            else:
                A[processing], A[unique] = A[unique], A[processing]
                unique += 1
        processing += 1
    return unique


@enable_executor_hook
def delete_duplicates_wrapper(executor, A):
    idx = executor.run(functools.partial(delete_duplicates, A))
    return A[:idx]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sorted_array_remove_dups.py",
                                       'sorted_array_remove_dups.tsv',
                                       delete_duplicates_wrapper))

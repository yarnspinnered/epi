import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    if size == 0:
        return 0
    left, middle, a_count = 0, 0,0
    while middle < size:
        if s[middle] == "a":
            a_count+=1
        if s[middle] == "b":
            s[middle] = ""
        else:
            s[left], s[middle] = s[middle], s[left]
            left += 1
        middle += 1

    read_i = left - 1
    write_i = left + a_count - 1

    while write_i >= 0:
        val = s[read_i]
        if val == "a":
            s[write_i - 1:write_i + 1] = "dd"
            write_i -= 2
        else:
            s[write_i] =val
            write_i -= 1
        read_i -= 1

    return left + a_count

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))

import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


def replace_and_remove(size, s):
    clean = 0
    num_a = 0
    for i in range(size):
        x = s[i]
        if x == "a":
            num_a += 1
        if x != "b":
            s[clean] = x
            clean += 1

    res = right_end = num_a + clean - 1
    for i in reversed(range(clean)):
        x = s[i]
        if x == "a":
            s[right_end], s[right_end - 1] = "d", "d"
            right_end -= 2
        else:
            s[right_end] = x
            right_end -= 1

    return res + 1

@enable_executor_hook
def replace_and_remove_wrapper(executor, size, s):
    res_size = executor.run(functools.partial(replace_and_remove, size, s))
    return s[:res_size]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("replace_and_remove.py",
                                       'replace_and_remove.tsv',
                                       replace_and_remove_wrapper))

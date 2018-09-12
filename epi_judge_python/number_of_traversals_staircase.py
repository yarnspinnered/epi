from test_framework import generic_test


def number_of_ways_to_top(top, maximum_step):
    # TODO - you fill in here.
    cache = [0 for i in range(top + 1)]
    cache[0] = 1

    for i in range(1, top + 1):
        for j in range(1, maximum_step + 1):
            if i - j >= 0:
                cache[i] += cache[i - j]
    return cache[top]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_staircase.py",
                                       "number_of_traversals_staircase.tsv",
                                       number_of_ways_to_top))

from test_framework import generic_test


def longest_contained_range(A):
    unprocessed = set(A)
    longest = 0

    while unprocessed:
        x = unprocessed.pop()
        l_x, r_x = x - 1, x + 1
        while l_x in unprocessed:
            unprocessed.remove(l_x)
            l_x -= 1
        while r_x in unprocessed:
            unprocessed.remove(r_x)
            r_x += 1
        longest = max(longest, r_x - l_x - 1)
    return longest


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("longest_contained_interval.py",
                                       'longest_contained_interval.tsv',
                                       longest_contained_range))

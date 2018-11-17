from test_framework import generic_test


def get_max_trapped_water(heights):
    def get_water(l,r):
        return (r - l) * min(heights[l], heights[r])
    l = 0
    r = len(heights) - 1
    best = 0
    while l < r:
        best = max(get_water(l,r), best)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return best


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_trapped_water.py",
                                       "max_trapped_water.tsv",
                                       get_max_trapped_water))

from test_framework import generic_test


def calculate_trapping_water(heights):
    max_h = heights.index(max(heights))

    def water_till_end(heights):
        running_sum , highest_so_far = 0, float('-inf')
        for h in heights:
            if h > highest_so_far:
                highest_so_far = h
            else:
                running_sum += highest_so_far - h
        return running_sum

    return water_till_end(heights[:max_h]) + water_till_end(reversed(heights[max_h + 1:]))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_water_trappable.py",
                                       'max_water_trappable.tsv',
                                       calculate_trapping_water))

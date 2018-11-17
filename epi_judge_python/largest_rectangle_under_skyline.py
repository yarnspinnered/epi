from test_framework import generic_test


def calculate_largest_rectangle(heights):
    s = []
    best = 0
    for i,h in enumerate(heights + [0]):
        while s and s[-1][1] > h:
            old_i, old_h  = s.pop()
            height = old_h
            width = i - s[-1][0] - 1 if s else i
            best = max(best, height * width)
        s.append((i,h))
    return best


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("largest_rectangle_under_skyline.py",
                                       'largest_rectangle_under_skyline.tsv',
                                       calculate_largest_rectangle))

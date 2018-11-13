import collections

from test_framework import generic_test
from test_framework.test_failure import PropertyName

Rectangle = collections.namedtuple('Rectangle', ('x', 'y', 'width', 'height'))


def intersect_rectangle(R1, R2):
    def check_for_intersect(r1, r2, r1_len, r2_len):
        if r1 <= r2 <= r1 + r1_len:
            return (r2, min(r1 + r1_len, r2 + r2_len)- r2)
        elif r2 <= r1 <= r2 + r2_len:
            return (r1, min(r1 + r1_len, r2 + r2_len) - r1)
        else:
            return None, None

    x, width = check_for_intersect(R1.x, R2.x, R1.width, R2.width)
    y, height = check_for_intersect(R1.y, R2.y, R1.height, R2.height)
    if not x is None and not y is None:
        return Rectangle(x, y, width, height)
    else:
        return Rectangle(0,0,-1,-1)


def intersect_rectangle_wrapper(R1, R2):
    return intersect_rectangle(Rectangle(*R1), Rectangle(*R2))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2], x[3]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "rectangle_intersection.py",
            'rectangle_intersection.tsv',
            intersect_rectangle_wrapper,
            res_printer=res_printer))

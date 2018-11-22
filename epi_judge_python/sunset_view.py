from test_framework import generic_test
from collections import namedtuple

def examine_buildings_with_sunset(sequence):
    active = []
    building = namedtuple("building", "height index")

    for i,b in enumerate(sequence):
        real_i = i
        while active and active[-1].height <= b:
            active.pop()
        active.append(building(b,real_i))
    return list(reversed(list(x.index for x in active)))


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))

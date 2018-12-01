import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook

HighwaySection = collections.namedtuple('HighwaySection',
                                        ('x', 'y', 'distance'))


def find_best_proposals(H, P, n):
    mat = [[float('inf') for _ in range(n)] for _ in range(n)]
    for i in range(n):
        mat[i][i] = 0
    for x,y,dist in H:
        mat[x][y] = dist
        mat[y][x] = dist

    for k in range(n):
        for i in range(n):
            for j in range(n):
                mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

    koth, best_reduction = None, float('-inf')
    for x,y,dist in P:
        reduction = 0
        for i in range(n):
            for j in range(n):
                delta = mat[i][j] - (mat[i][x] + dist + mat[y][j])
                if delta > 0:
                    reduction += delta
        if reduction > best_reduction:
            best_reduction = reduction
            koth = HighwaySection(x,y,dist)

    return koth


@enable_executor_hook
def find_best_proposals_wrapper(executor, H, P, n):
    H = [HighwaySection(*x) for x in H]
    P = [HighwaySection(*x) for x in P]

    return executor.run(functools.partial(find_best_proposals, H, P, n))


def res_printer(prop, value):
    def fmt(x):
        return [x[0], x[1], x[2]] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "road_network.py",
            'road_network.tsv',
            find_best_proposals_wrapper,
            res_printer=res_printer))

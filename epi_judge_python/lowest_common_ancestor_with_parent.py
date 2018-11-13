import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    def depth(u):
        d = 0
        while u.parent != None:
            d += 1
            u = u.parent
        return d

    path0, path1 = depth(node0), depth(node1)
    diff = abs(path0 - path1)
    if path0 > path1:
        for i in range(diff):
            node0 = node0.parent
    else:
        for i in range(diff):
            node1 = node1.parent

    while not node0 is node1:
        node0 = node0.parent
        node1 = node1.parent
    return node0

@enable_executor_hook
def lca_wrapper(executor, tree, node0, node1):
    result = executor.run(
        functools.partial(lca, must_find_node(tree, node0),
                          must_find_node(tree, node1)))

    if result is None:
        raise TestFailure("Result can't be None")
    return result.data


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lowest_common_ancestor_with_parent.py",
                                       'lowest_common_ancestor.tsv',
                                       lca_wrapper))

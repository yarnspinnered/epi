import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def lca(node0, node1):
    seen = set()

    while not node0 is None or not node1 is None:
        if node0 in seen:
            return node0
        else:
            if not node0 is None:
                seen.add(node0)
                node0 = node0.parent
        if node1 in seen:
            return node1
        else:
            if not node1 is None:
                seen.add(node1)
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
        generic_test.generic_test_main(
            "lowest_common_ancestor_close_ancestor.py",
            'lowest_common_ancestor.tsv', lca_wrapper))

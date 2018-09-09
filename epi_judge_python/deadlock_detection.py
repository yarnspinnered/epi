import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from enum import Enum

class GraphVertex:
    def __init__(self):
        self.edges = []
        self.color = Color.WHITE

class Color(Enum):
    WHITE = 0
    GREY = 1
    BLACK = 2

def is_deadlocked(graph):
    def DFS(s):
        def helper(curr):
            flag = False
            for e in curr.edges:
                if e.color == Color.WHITE:
                    e.color = Color.GREY
                    flag = helper(e)
                elif e.color == Color.GREY:
                    return True
            curr.color = Color.BLACK
            return flag

        return helper(s)

    graph[0].color = Color.GREY
    return DFS(graph[0])


@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("deadlock_detection.py",
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))

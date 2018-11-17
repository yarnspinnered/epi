import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from enum import Enum
from collections import deque
class Color(Enum):
    UNCOLORED = 0
    WHITE = 1
    BLACK = 2

class GraphVertex:
    def __init__(self):
        self.d = -1
        self.edges = []
        self.color = Color.UNCOLORED

def is_any_placement_feasible(graph):


    def dfs(u):
        # print(u.d, u.edges, u.color)

        uncolorable = False
        other_col = Color.WHITE if u.color == Color.BLACK else Color.BLACK
        for nbr in u.edges:
            if nbr.color == u.color and u.color != Color.UNCOLORED:
                uncolorable = True
            else:
                if nbr.color == Color.UNCOLORED:
                    nbr.color = other_col
                    uncolorable |= dfs(nbr)


        return uncolorable

    res = False
    for g in graph:
        if g.color == Color.UNCOLORED:
            g.color = Color.WHITE
            res |= dfs(g)

    return not res
    # def BFS(start):
    #     start.color = Color.WHITE
    #     explored.add(start)
    #     q = deque()
    #     q.append((0,start))
    #
    #     while q:
    #         curr_level, curr = q.popleft()
    #         for e in curr.edges:
    #
    #             if curr_level % 2 == 0:
    #                 next_color = Color.BLACK
    #             else:
    #                 next_color = Color.WHITE
    #             if e not in explored:
    #                 explored.add(e)
    #                 e.color = next_color
    #                 q.append((curr_level + 1, e))
    #             else:
    #                 if e.color == curr.color:
    #                     return False
    #     return True
    # explored = set()
    # return all([BFS(x) for x in graph if x.color == Color.UNCOLORED])


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_circuit_wirable.py",
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))

import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:
    def __init__(self):
        self.edges = []
        # Set max_distance = 0 to indicate unvisitied vertex.
        self.max_distance = 0


def find_largest_number_teams(graph):
    def dfs(u):
        u.max_distance = 1
        for nbr in u.edges:
            if nbr.max_distance == 0:
                dfs(nbr)
            u.max_distance = max(u.max_distance, nbr.max_distance + 1)
        return
    any(dfs(g) for g in graph if g.max_distance == 0)
    return max(g.max_distance for g in graph)
    # def DFS(curr):
    #     curr.max_distance = max(((v.max_distance if v.max_distance > 0 else DFS(v)) + 1 for v in curr.edges), default=1)
    #     return curr.max_distance
    #
    #
    # return max(DFS(g) for g in graph if g.max_distance == 0)


@enable_executor_hook
def find_largest_number_teams_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(find_largest_number_teams, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("max_teams_in_photograph.py",
                                       'max_teams_in_photograph.tsv',
                                       find_largest_number_teams_wrapper))

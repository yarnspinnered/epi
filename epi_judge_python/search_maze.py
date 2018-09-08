import collections
import copy
import functools
import heapq

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook

WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

#DFS: explored set, prev data structure. A helper function marks current node explored then calls DFS on unexplored nbrs and updates prev
def DFS(maze, s, e):
    def helper(src):
        possible_directions = [Coordinate(src.x - 1, src.y),
                               Coordinate(src.x + 1, src.y),
                               Coordinate(src.x, src.y - 1),
                               Coordinate(src.x, src.y + 1)]
        explored[src.x][src.y] = True

        for dir in possible_directions:
            if path_element_is_feasible(maze, src, dir) and explored[dir.x][dir.y] != True:
                prev[dir] = src
                helper(dir)

    if not maze:
        return []
    explored = [[False for x in maze[0]] for y in maze]
    explored[s.x][s.y] = True
    prev = {s : None}

    helper(s)

    res = collections.deque()
    if e in prev:
        curr = e
        while curr:
            res.appendleft(curr)
            curr = prev[curr]

    return list(res)

#BFS : Queue, a prev map and an explored set. Get node from q, immediately mark it explored, add stuff to q and update the prev at same time
def BFS(maze, s, e):
    q = collections.deque([(0,s)])
    prev = {s : None}
    explored = set([s])

    while q:
        level, curr = q.pop()

        if curr == e:
            break
        curr_level = explored.add(curr)
        possible_directions = [Coordinate(curr.x - 1, curr.y),
                               Coordinate(curr.x + 1, curr.y),
                               Coordinate(curr.x, curr.y - 1),
                               Coordinate(curr.x, curr.y + 1)]
        for next in possible_directions:
            if path_element_is_feasible(maze, curr, next) and next not in explored:
                q.appendleft((level + 1, next))
                prev[next] = curr


    res = collections.deque()
    if e in prev:
        curr = e
        while curr:
            res.appendleft(curr)
            curr = prev[curr]

    return list(res)



def search_maze(maze, s, e):
    return BFS(maze, s, e)


def path_element_is_feasible(maze, prev, cur):
    if not ((0 <= cur.x < len(maze)) and
            (0 <= cur.y < len(maze[cur.x])) and maze[cur.x][cur.y] == WHITE):
        return False
    return cur == (prev.x + 1, prev.y) or \
           cur == (prev.x - 1, prev.y) or \
           cur == (prev.x, prev.y + 1) or \
           cur == (prev.x, prev.y - 1)


@enable_executor_hook
def search_maze_wrapper(executor, maze, s, e):
    s = Coordinate(*s)
    e = Coordinate(*e)
    cp = copy.deepcopy(maze)

    path = executor.run(functools.partial(search_maze, cp, s, e))

    if not path:
        return s == e

    if path[0] != s or path[-1] != e:
        raise TestFailure("Path doesn't lay between start and end points")

    for i in range(1, len(path)):
        if not path_element_is_feasible(maze, path[i - 1], path[i]):
            raise TestFailure("Path contains invalid segments")

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_maze.py", 'search_maze.tsv',
                                       search_maze_wrapper))

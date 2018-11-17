import collections
import copy
import functools
import heapq

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook
from collections import deque
WHITE, BLACK = range(2)

Coordinate = collections.namedtuple('Coordinate', ('x', 'y'))

#DFS: explored set, prev data structure. A helper function marks current node explored then calls DFS on unexplored nbrs and updates prev
def DFS(maze, s, e):
    res = deque()
    seen = set()
    def helper(s):
        if s == e:
            res.appendleft(s)
            return True
        for a,b in [(0,1), (0, -1), (1,0), (-1, 0)]:
            if 0 <= s.y + a < len(maze[0]) and \
                0 <= s.x + b < len(maze) and \
                maze[s.x + b][s.y + a] == 0 and \
                Coordinate(s.x + b, s.y + a) not in seen:
                seen.add(Coordinate(s.x + b, s.y + a))
                if helper(Coordinate(s.x + b, s.y + a)):
                    res.appendleft(s)
                    return True
        return False
    helper(s)
    return res

#BFS : Queue, a prev map and an explored set. Get node from q, immediately mark it explored, add stuff to q and update the prev at same time
def BFS(maze, s, e):
    q = deque()
    explored = {}
    q.append(s)
    explored[s] = None
    while q:
        s = q.pop()
        for a, b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_coord = Coordinate(s.x + b, s.y + a)
            if 0 <= s.y + a < len(maze[0]) and \
                    0 <= s.x + b < len(maze) and \
                    maze[s.x + b][s.y + a] == 0 and \
                    new_coord not in explored:
                explored[new_coord] = s
                q.appendleft(new_coord)
    res = deque()
    while e in explored:
        res.appendleft(e)
        e = explored[e]
    return res


def search_maze(maze, s, e):
    return DFS(maze,s,e)


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

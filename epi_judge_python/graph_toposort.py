import enum
from collections import defaultdict, deque, Counter

class Color(enum.Enum):
    WHITE = 0
    GRAY = 1
    BLACK = 2


class Graph():

    def __init__(self, matrix):
        self.graph = defaultdict(dict)
        for i,row in enumerate(matrix):
            self.graph[i] = {}
            for j,x in enumerate(row):
                if x > 0:
                    self.graph[i][j] = 1

    def addEdge(self, s, t):
        self.graph[s][t] = 1

    def toposort(self):
        explored = {}
        res = deque()
        def dfs(s):
            if s in explored:
                if explored[s] == Color.BLACK:
                    return True
                elif explored[s] == Color.GRAY:
                    return False

            explored[s] = Color.GRAY
            for nbr, _ in self.graph[s].items():
                if not dfs(nbr):
                    return False
            explored[s] = Color.BLACK

            res.appendleft(s)
            return True
        vertices = set(x for x in self.graph)
        vertices2 = set(v for k in self.graph for v in self.graph[k])
        vertices = vertices.union(vertices2)
        for u in vertices:
            if u not in explored:
                if not dfs(u):
                    return False

        return res





g = Graph([])
g.addEdge(5,11)
g.addEdge(7,11)
g.addEdge(7,8)
g.addEdge(3,8)
g.addEdge(3,10)
g.addEdge(11,2)
g.addEdge(11,9)
g.addEdge(11,10)
g.addEdge(8,9)
print(g.toposort())
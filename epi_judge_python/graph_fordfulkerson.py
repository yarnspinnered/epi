
from collections import defaultdict, namedtuple, deque

Edge = namedtuple("Edge", "forward backward")
class Graph():

    def __init__(self, matrix):
        self.graph = defaultdict(dict)
        for i,row in enumerate(matrix):
            for j,x in enumerate(row):
                if x > 0:
                    self.graph[i][j] = Edge(x, 0)

    def bfs(self, s, t):
        q = deque()
        prev = {s : None}
        q.append(s)

        while q:
            curr = q.popleft()
            for nbr, e in self.graph[curr].items():
                if nbr not in prev and e.forward > 0:
                    q.append(nbr)
                    prev[nbr] = curr
            if t in prev:
                break
        if t in prev:
            return prev
        else:
            return None

    def augment(self, parents, s, t):
        end = t
        curr  = parents[end]
        smallest_residual = float('inf')
        to_augment = []
        while not curr is None:

            to_augment.append((curr,end))
            residual, flow = self.graph[curr][end]
            smallest_residual = min(smallest_residual, residual)
            curr, end = parents[curr], curr

        for u,v in to_augment:
            old_f, old_b = self.graph[u][v]
            print("augmenting: ", u, v, old_f, old_b)
            self.graph[u][v] = Edge(old_f - smallest_residual, old_b + smallest_residual)

        return smallest_residual


    def fordfulkerson(self, s, t):
        flow = 0
        parents = self.bfs(s,t)

        while parents:
            flow += self.augment(parents, s, t)
            parents = self.bfs(s, t)
        print("flow: ", flow)

        print(self.graph)
        return flow




g = Graph([[0, 16, 13, 0, 0, 0],
           [0, 0, 10, 12, 0, 0],
           [0, 4, 0, 0, 14, 0],
           [0, 0, 9, 0, 0, 20],
           [0, 0, 0, 7, 0, 4],
           [0, 0, 0, 0, 0, 0]
           ])
print(g.graph)
print(g.bfs(0,5))
g.fordfulkerson(0,5)
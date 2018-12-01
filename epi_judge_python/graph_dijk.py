from collections import defaultdict

class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, src, dest, weight):
        newNode = (dest, weight)
        self.graph[src].insert(0, newNode)

        newNode = (src, weight)
        self.graph[dest].insert(0, newNode)

    def printNbrs(self, x):
        print(self.graph[x])

    def dijkstra(self,s,t):
        n = sum(len(node_d) for node_d in self.graph.values())//2
        d = [float('inf') for _ in range(n)]
        d[s] = 0
        intree = set([s])
        for v, w in self.graph[s]:
            d[v] = d[s] + w


        for i in range(n):
            prev, next, weight = None, None, float('inf')
            for u in intree:
                for v, w in self.graph[u]:
                    if v not in intree and (next is None or d[v] < d[next]):
                        next = v
                        prev = u
                        weight = w
            if next == None:
                break
            intree.add(next)

            d[next] = min(d[next], weight + d[prev])
            for u, w in self.graph[next]:
                d[u] = min(d[u], d[next] + w)
            print(prev,next,weight)
            print(d)
        return d[t]

#
# 0                0
# 1                4
# 2                12
# 3                19
# 4                21
# 5                11
# 6                9
# 7                8
# 8                14
graph = Graph(9)
graph.addEdge(0, 1, 4)
graph.addEdge(0, 7, 8)
graph.addEdge(1, 2, 8)
graph.addEdge(1, 7, 11)
graph.addEdge(2, 3, 7)
graph.addEdge(2, 8, 2)
graph.addEdge(2, 5, 4)
graph.addEdge(3, 4, 9)
graph.addEdge(3, 5, 14)
graph.addEdge(4, 5, 10)
graph.addEdge(5, 6, 2)
graph.addEdge(6, 7, 1)
graph.addEdge(6, 8, 6)
graph.addEdge(7, 8, 7)

print(graph.dijkstra(0,5))

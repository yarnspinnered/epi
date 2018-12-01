from collections import defaultdict, namedtuple

Edge = namedtuple("Edge", "src dst name")

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)



    def addEdge(self, s, t, name):
        self.graph[s].append(Edge(s,t, name))
        self.graph[t].append(Edge(t,s, name))

    def eulerian_walk(self, start):
        res = []
        s = []

        def walk( u):
            s.append(u)
            src, curr, name = self.graph[u].pop()
            self.graph[curr].remove(Edge(curr, src, name))
            s.append(curr)
            while curr != u:
                print("curr: ", curr)
                print(s, res, self.graph)
                src, curr, name = self.graph[curr].pop()
                self.graph[curr].remove(Edge(curr, src, name))
                s.append(curr)


        walk(start)
        print(s, res)
        while s:
            curr = s.pop()
            if self.graph[curr]:
                walk(curr)
            else:
                res.append(curr)
        print(res)
        return res




g = Graph()
# g.addEdge(0,1, 'b')
# g.addEdge(1,3, 'e')
# g.addEdge(2,0, 'd')
# g.addEdge(1,2, 'a')
# g.addEdge(4,1, 'f')
# g.addEdge(3,4, 'f')


# g.addEdge(0,1, 'b')
# g.addEdge(0,2, 'e')
# g.addEdge(0,4, 'd')
# g.addEdge(0,5, 'a')
# g.addEdge(1,2, 'f')
# g.addEdge(1,3, 'g')
# g.addEdge(1,4, 'c')
# g.addEdge(2,3, 'h')
# g.addEdge(2,4, 'i')
# g.addEdge(3,4, 'j')
# g.addEdge(3,5, 'k')
g.eulerian_walk(0)
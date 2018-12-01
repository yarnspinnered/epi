class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def floyd(self):
        res = [[ x for x in row] for row in self.graph]

        for k in range(self.V):
            for j in range(self.V):
                for i in range(self.V):
                    through_k = res[i][k]  + res[k][j]
                    res[i][j] = min(res[i][j], through_k)

        print(res)
        return res
g = Graph(4)
INF = float('inf')
g.graph = [[0,5,INF,10],
             [INF,0,3,INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
        ]

g.floyd()
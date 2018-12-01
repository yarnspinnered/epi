import sys  # Library for INT_MAX
from collections import namedtuple


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

        # A utility function to print the constructed MST stored in parent[]

    def printMST(self, parent):
        print("Edge \tWeight")

        for i in range(1, self.V):
            print(parent[i], "-", i, "\t", self.graph[i][parent[i]])


            # A utility function to find the vertex with

    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minKey(self, key, mstSet):

        # Initilaize min value
        min = sys.maxsize

        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self):
        l = []
        weight_edge = namedtuple("weight_edge", "weight edge")
        for i, row in enumerate(self.graph):
            for j, x in enumerate(row):
                if x > 0:
                    l.append(weight_edge(x,(i,j)))
        l.sort()
        res = []
        seen_nodes = set()
        res.append(l[0].edge)
        print(res)
        seen_nodes.add(l[0].edge[0])
        seen_nodes.add(l[0].edge[1])

        print(seen_nodes)
        for w, e in l[1:]:
            count =(1 if  e[0] in seen_nodes else 0) + (1 if e[1] in seen_nodes else 0)
            if count == 1:
                res.append(e)
                seen_nodes.add(e[0])
                seen_nodes.add(e[1])

        print(res)



g = Graph(5)
g.graph = [[0, 2, 0, 6, 0],
           [2, 0, 3, 8, 5],
           [0, 3, 0, 0, 7],
           [6, 8, 0, 0, 9],
           [0, 5, 7, 9, 0]]
#
# 0 - 1    2
# 1 - 2    3
# 0 - 3    6
# 1 - 4    5
g.primMST();

class union_find:
    def __init__(self, n):
        self.subsets = [i for i in range(n)]
        self.sizes = [1 for i in range(n)]

    def union(self, x, y):
        r_x, r_y = self.find(x), self.find(y)
        if r_x == r_y:
            return
        else:
            if self.sizes[r_x] > self.sizes[r_y]:
                self.subsets[r_y] = r_x
                self.sizes[r_x] += self.sizes[r_y]
            else:
                self.subsets[r_x] = r_y
                self.sizes[r_y] += self.sizes[r_x]

    def find(self,x):
        if self.subsets[x] == x:
            return x
        else:
            return self.find(self.subsets[x])

uf = union_find(10)
uf.union(1,2)
uf.union(3,4)
uf.union(5,6)
uf.union(2,3)
uf.union(5,3)
uf.union(7,8)
uf.union(7,1)
print("subsets: ", uf.subsets)
print("sizes  : ", uf.sizes)
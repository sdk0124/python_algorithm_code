class UnionFind_byRank:
    def __init__(self, roots):
        self.roots = roots
        self.ranks = [0] * len(self.roots)

    def set_rank(self):
        for i in range(len(self.roots)):
            self.ranks[i] = 1

    def find(self, vertex):
        while (vertex != self.roots[vertex]):
            vertex = self.roots[vertex]
        return vertex
    
    def union(self, vertex1, vertex2):
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        if (root1 != root2):
            if (self.ranks[root1] > self.ranks[root2]):
                self.roots[root2] = root1
            elif (self.ranks[root1] < self.ranks[root2]):
                self.roots[root1] = root2
            else:
                self.roots[root2] = root1
                self.ranks[root1] += 1

    def connected(self, v1, v2):
        return self.find(v1) == self.find(v2)
    
vertex_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
count = 10
unionfind_byrank = UnionFind_byRank(vertex_list)
unionfind_byrank.set_rank()

#(2, 7)
#(3, 8)
#(4, 9)
#(6, 7)
#(7, 3)
#(9, 8)
#(0, 1)
#(5, 0)
#(6, 0)
#(9, 5)

for i in range(count):
    v1 = int(input())
    v2 = int(input())
    unionfind_byrank.union(v1, v2)
    print("Union ok")

print(unionfind_byrank.roots)
print(unionfind_byrank.ranks)
print(unionfind_byrank.connected(0, 4))
print(unionfind_byrank.connected(2, 7))
print(unionfind_byrank.connected(3, 9))

# rank와 height는 다르다.
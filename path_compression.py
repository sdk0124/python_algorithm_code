class PathCompression:
    def __init__(self, roots):
        self.roots = roots

    def find(self, vertex):
        if (vertex != self.roots[vertex]):
            self.roots[vertex] = self.find(self.roots[vertex])
        return self.roots[vertex]
        # if (vertex == self.roots[vertex]):
        #     return vertex
        # self.roots[vertex] = self.find(self.roots[vertex])

    def union(self, v1, v2):
        root1 = self.find(v1)
        root2 = self.find(v2)
        if (root1 != root2):
            self.roots[root2] = root1

    def connected(self, v1, v2):
        return self.find(v1) == self.find(v2)
    
path_c = PathCompression([1, 2, 3, 3, 5, 5])

#(0, 4)

count = 1
for i in range(count):
    v1 =  int(input())
    v2 = int(input())
    path_c.union(v1, v2)
    print("union ok")

print(path_c.roots)
print(path_c.connected(0, 4))
class DisjointSet:
    def __init__(self, vertexs):
        self.parent_vertexs = [p for p in vertexs]

    def union(self, vertex1, vertex2):
        self.parent_vertexs[vertex2] = vertex1

    def find(self, vertex):
        return self.parent_vertexs[vertex]

    def connected(self, vertex1, vertex2):
        if (self.find(vertex1) == self.find(vertex2)):
            return True
        elif (self.find(vertex1) == vertex1 and self.find(vertex2) == vertex2 and self.find(vertex1) != self.find(vertex2)):
            return False
        else:
            return self.connected(self.find(vertex1), self.find(vertex2))

vertexs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

d_set = DisjointSet(vertexs)

for t in range(6):
    v1 = int(input())
    v2 = int(input())
    d_set.union(v1, v2)
    print("Union 완료")

print(d_set.connected(0, 3))
print(d_set.connected(1, 5))
print(d_set.connected(7, 8))
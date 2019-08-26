# The time complexity for the matrix representation is O(V^2).
# In this post, O(ELogV) algorithm for adjacency list representation is discussed.
# As discussed in the previous post, in Prim’s algorithm, two sets are maintained,
# one set contains list of vertices already included in MST, other set contains vertices not 
# yet included. With adjacency list representation, all vertices of a graph can be traversed in O(V+E) 
# time using BFS. The idea is to traverse all vertices of graph using BFS and use a Min Heap to store the 
# vertices not yet included in MST. Min Heap is used as a priority queue to get the minimum weight edge from 
# the cut. Min Heap is used as time complexity of operations like extracting minimum element and decreasing key 
# value is O(LogV) in Min Heap.

class Graph(object):
    def __init__(self, matrix):
        self.graph = matrix
        self.num_vertices = len(matrix)
        self.ancestor = [None]*self.num_vertices

    def printPath(self, vertex):
        ancestor = self.ancestor[vertex]
        stack = []
        
        while ancestor != None:
            stack.append(ancestor)
            ancestor = self.ancestor[ancestor]
        print(stack)

    def printAncestor(self):
        print(self.ancestor)

    def primMin(self, key, mstSet):
        min = float("inf")
        for i in range(self.num_vertices):
            if key[i] < min and mstSet[i] == False:
                min = key[i]
                min_index = i
        return min_index

    def primMST(self, src):
        key = [float("inf")]*self.num_vertices
        key[src] = 0
        mstSet = [False]*self.num_vertices

        for _ in range(self.num_vertices):
            u = self.primMin(key, mstSet)
            mstSet[u] = True

            for v in range(self.num_vertices):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    self.ancestor[v] = u

if __name__ == "__main__":
     
    matrix =  [ [0, 2, 0, 6, 0], 
                [2, 0, 3, 8, 5], 
                [0, 3, 0, 0, 7], 
                [6, 8, 0, 0, 9], 
                [0, 5, 7, 9, 0]]
    g = Graph(matrix)
    g.primMST(0)
    g.printPath(4)
    g.printAncestor()
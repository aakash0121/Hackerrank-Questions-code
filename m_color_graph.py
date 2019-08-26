class Node(object):
    def __init__(self, matrix, vertices, m):
        self.num_colors = m
        self.vertices = vertices
        self.graph = matrix
        self.color = [None]*self.vertices
    
    def printVertexColor(self):
        return self.color
    
    def isSafe(self, v, c):
        for i in self.vertices:
            if self.graph[v][i] == 1 and self.color == c:
                return False
            
        return True
    
    def graphColoUtil(self, v):
        if v >= self.vertices:
            return True
        
        for c in range(1, self.num_colors+1):
            if self.isSafe(v, c):
                self.color[v] = c

                if self.graphColorUtil(v+1):
                    return True
                self.color[v] = 0
    
            
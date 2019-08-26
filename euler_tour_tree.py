class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
    
    def setParent(self, parent):
        self.parent = parent
    
    def setLeft(self, left):
        self.left = left
    
    def setRight(self, right):
        self.right = right
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right
    
    def getData(self):
        return self.data
    
    def getParent(self):
        return self.parent    
    
class Tree:
    def __init__(self, n):
        self.visited = [False]*n

    def euler_tour(self, root):
        if root is not None:
            print(root.data, end = " ")
            self.visited[root.data] = True
            if root.left is not None and self.visited[root.left.data] == False:
                self.visited[root.left.data] = True
                return self.euler_tour(root.left)
            elif root.right is not None and self.visited[root.right.data] == False:
                self.visited[root.right.data] = True
                return self.euler_tour(root.right)
            else:
                return self.euler_tour(root.parent)
        else:
            print()

if __name__ == "__main__":
    root = Node(0)

    root.setLeft(Node(1))
    root.left.setParent(root)

    root.left.setLeft(Node(2))
    root.left.left.setParent(root.left)

    root.left.setRight(Node(3))
    root.left.right.setParent(root.left)

    root.left.left.setLeft(Node(4))
    root.left.left.left.setParent(root.left.left)

    n = 5
    t = Tree(n)
    t.euler_tour(root)
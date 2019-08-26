class Node(object):
    def __init__(self, data, parent = None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

n1_ref = None
n2_ref = None
    
class LCA(object):
    def __init__(self, root, n1, n2):
        self.root = root
        self.n1 = n1
        self.n2 = n2
        self.n1_ancestors = []
        self.n2_ancestors = []
    
    def preorder_traversal(self, root, n1, n2):
        global n1_ref, n2_ref

        if root:
            if root.data == n1:
                n1_ref = root
            if root.data == n2:
                n2_ref = root

            print(root.data, end  = " ")
            if root.left != None:
                root.left.parent = root
            self.preorder_traversal(root.left, n1, n2)

            if root.right != None:
                root.right.parent = root
            self.preorder_traversal(root.right, n1, n2)
        return n1_ref, n2_ref

    def compute_LCA(self):
        if self.root is None:
            return None

        n1, n2 = self.preorder_traversal(self.root, self.n1, self.n2)
        self.n1_ancestors.append(n1.data)
        self.n2_ancestors.append(n2.data)
        while n1.parent != None:
            self.n1_ancestors.append(n1.parent.data)
            n1 = n1.parent
        
        while n2.parent != None:
            self.n2_ancestors.append(n2.parent.data)
            n2 = n2.parent
        
        for i in self.n1_ancestors:
            for j in self.n2_ancestors:
                if i == j:
                    return i

if __name__ == "__main__":
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(4)
    root.left.right = Node(12)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    n1, n2 = map(int, input("enter the data of two nodes: ").split())
    lca = LCA(root, n1, n2)
    commom_ancestor = lca.compute_LCA()
    print()
    print(commom_ancestor)
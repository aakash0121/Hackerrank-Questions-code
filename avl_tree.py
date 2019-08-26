class Node(object):
    def __init__(self, value):
        self.value = value
        self.height = 1
        self.left = None
        self.right = None
    
class avl(object):

    def getHeight(self, root):
        if not root:
            return 0
        return root.height
    
    def getBalance(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        
        # perform rotation
        y.left = z
        z.right = T2

        # updates Heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y
    
    def rightRotate(self, z):
        y = z.left
        T3 = y.right

        #perform rotation
        y.right = z
        z.left = T3

        # updates Heights
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y
    
    def getMinValNode(self, root):
        if root is None or root.left is None:
            return root
        return getMinValNode(root.left)

    def insert(self, root, value):
        # perform normal BST
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        # update the height of ancester node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
        
        # get the balance factor
        balance = self.getBalance(root)

        # if the tree is unbalanced:

        if balance > 1:
            # case 1: Left-Left
            if value < root.left.value:
                return self.rightRotate(root)
            # case 2: Left-Right
            elif value > root.left.value:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        
        if balance < -1:
            # case 3: Right-Right
            if value > root.right.value:
                return self.leftRotate(root)
            # case 4: Right-Left
            elif value < root.right.value:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)
        
        return root
    
    def delete(self, root, value):
        # perform standard BST delete
        if not root:
            return root
        elif value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            elif root.right is None:
                temp = root.left
                root = None
                return temp
        
        temp = self.getMinValNode(root.right)
        root.value = temp.value
        root.right = self.delete(root.right, temp.value)

        if root is None:
            return root
        
        # update the height of ancestor node
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

        # get the balance factor
        balance = self.getBalance(root)

        # balancing the node(if unbalanced)
        if balance > 1:
            # case 1: Left-Left
            if self.getBalance(root.left) >= 0:
                return self.rightRotate(root)
            #case2: Left-Right
            if self.getBalance(root.left) < 0:
                root.left = self.leftRotate(root.left)
                return self.rightRotate(root)
        elif balance < -1:
            # case 3: Right-Right
            if self.getBalance(root.right) >= 0:
                return self.leftRotate(root)
            # case 4: Right-Left
            if self.getBalance(root.right) < 0:
                root.right = self.rightRotate(root.right)
                return self.leftRotate(root)

        return root 

    def preOrder(self, root):
        if root is None:
            return
        print("{}".format(root.value), end = " ")
        self.preOrder(root.left)
        self.preOrder(root.right)

myTree = avl()
root = None
nums = [9, 5, 10, 0, 6, 11, -1, 1, 2] 
  
for num in nums: 
    root = myTree.insert(root, num) 
  
# Preorder Traversal 
print("Preorder Traversal after insertion -") 
myTree.preOrder(root) 
print() 
  
# Delete 
key = 10
root = myTree.delete(root, key) 
  
# Preorder Traversal 
print("Preorder Traversal after deletion -") 
myTree.preOrder(root) 
print()  
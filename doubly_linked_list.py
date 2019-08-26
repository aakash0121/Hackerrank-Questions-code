class Node(object):
    
    def __init__(self, data, previous = None, next = None):
        self.data = data
        self.previous = previous
        self.next = next
    
class DoublyLinkedList(object):
    
    def __init__(self):
        self.head = None
    
    def traverse(self):
        if self.head == None:
            print("linked list is empty")
            return

        temp = self.head
        while (temp != None):
            print(temp.data, end = ' ')
            temp = temp.next
            print("\n")

    def insert_at_start(self, data):
        newNode = Node(data)

        if self.head == None:
            self.head = newNode
        else:
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
    
    def insert_at_end(self, data):
        newNode = Node(data)

        if self.head == None:
            insert_at_start(data)
        else:
            temp = self.head
            while (temp != None):
                newNode.previous = temp
                temp.next = newNode

    def insert_in_between(self, previousData, data):
        newNode = Node(data)
        temp = self.head
        while (temp != None):
            if temp.data == previousData:
                break
        else:
            print("the previous data you entered in invalid")
            return
        newNode.next = temp.next
        newNode.previous = temp
        temp.next = newNode
    
    def delete(self, data):
        if self.head == None:
            print("linked list is empty")
            return
        
        temp = self.head
        while (temp != None):
            if temp.data == data:
                break
            temp = temp.next
        else:
            print("data you entered is invalid")
            return        

        if temp.next != None:
            temp.previous.next = temp.next
            temp.next.previous = temp.previous
        else:
            temp.previous.next = None
            temp.previous = None

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_in_between(3, 3)
    dll.insert_at_start(1)
    dll.insert_in_between(1, 2)
    dll.traverse()
    dll.delete(3)
    dll.delete(2)
    dll.traverse()
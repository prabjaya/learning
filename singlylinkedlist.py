class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.first = None
        self.last = None

    def add(self,data):
        node = Node(data)

        if self.first is None:
            self.first = node
        else: 
            self.last.next = node

        self.last = node
        

    def read(self):
        current = self.first

        while current != None:
            print(current.data)
            current = current.next
        print()


lst = Linkedlist()
lst.add(1)
lst.add(2)
lst.add(3)
lst.read()

    

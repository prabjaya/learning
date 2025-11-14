class Treenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def isFull(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True

    if node.left is not None and node.right is not None:
        leftcheck  = isFull(node.left)
        rightcheck = isFull(node.right)
        if leftcheck and rightcheck:
            return True
        else:
            return False
    return False


root = Treenode(10)
n1 = Treenode(20)
n2= Treenode(30)
n3 = Treenode(40)
n4 = Treenode(50)
n5 = Treenode(60)
n6 = Treenode(70)
n7 = Treenode(80)
n8 = Treenode(90)
n9 = Treenode(100)

root.left = n1
root.right = n2

n1.left =n3
n1.right = n4

n2.left = n5
# n2.right = n6

flag = isFull(root)
print(flag)
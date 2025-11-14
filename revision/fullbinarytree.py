class Treenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isfull(node):
    if node is None:
        return True
    if node.left is None and node.right is None:
        return True
    if node.left is not None and node.right is not None:
        leftcheck = isfull(node.left)
        rightcheck = isfull(node.right)
        if leftcheck and rightcheck:
            return  True
        else:
            return False
    return False


n1 = Treenode(10)

n1.left = Treenode(20)
n1.right = Treenode(30)


n1.left.left = Treenode(40)
n1.left.right = Treenode(50)


check = isfull(n1)
print(check)
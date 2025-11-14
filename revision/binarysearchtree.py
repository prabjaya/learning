class TreenNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def isBST(node):
    return isBSTUtil(node,float('-inf'),float('inf'))

def isBSTUtil(node,min,max):
    if node is None:
        return True
    if node.data <= min or node.data >= max:
        return False

    return isBSTUtil(node.left,min,node.data) and isBSTUtil(node.right,node.data,max)


n1 = TreenNode(100)

n1.left = TreenNode(50)
n1.right = TreenNode(400)


print(isBST(n1))
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.data)
    inorder(node.right)

n1 = TreeNode(1)
n1.left =TreeNode(2)
n1.left.left = TreeNode(4)
n1.left.right = TreeNode(5)
n1.right = TreeNode(3)
n1.right.left = TreeNode(40)
n1.right.right =TreeNode(50)
inorder(n1)

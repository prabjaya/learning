class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def preorder(node):
    if node is None:
        return

    print(node.data)
    preorder(node.left)
    preorder(node.right)



n1 = TreeNode(1)

n1.left =TreeNode(2)
n1.right =TreeNode(3)


n1.left.left = TreeNode(4)
n1.left.right = TreeNode(5)


n1.right.left = TreeNode(6)
n1.right.right=TreeNode(7)

preorder(n1)
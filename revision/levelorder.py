class TreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None


def levelorder(node):
    queue = [node]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current.data)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)



n1 = TreeNode(1)

n1.left=TreeNode(2)
n1.right=TreeNode(3)

n1.left.left = TreeNode(4)
n1.left.right =TreeNode(5)

n1.right.left = TreeNode(6)
n1.right.right=TreeNode(7)


levelorder(n1)
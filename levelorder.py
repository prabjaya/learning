class TreeNode:
    def __init__(self,val = 0):
        self.val = val
        self.left = None
        self.right = None


def levelorder(node):
    queue = [node]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current.val)
        if current.left is not None:
            queue.append(current.left)
        if current.right is not None:
            queue.append(current.right)
    

n1 = TreeNode(1)

n1.left =TreeNode(2)
n1.right = TreeNode(3)

n1.right.left = TreeNode(4)
n1.right.right = TreeNode(5)

levelorder(n1)
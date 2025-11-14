class TreeNode:
    def __init__(self,val = 0):
        self.val = val
        self.left = None
        self.right = None

def isBST(node):
    return isBSTUtil(node, float('-inf'), float('inf'))


def isBSTUtil(node, mini,maxi):
    if node is None:
        return True
    if node.val <= mini or node.val >= maxi:
        return False
    return isBSTUtil(node.left,mini,node.val -1) and isBSTUtil(node.right,node.val + 1, maxi)



n1 = TreeNode(100)
n1.left = TreeNode(50)
n1.right = TreeNode(150)

print(isBST(n1))



class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

N = int(input()) # 7
tree_dic = {}

for _ in range(N):
    root, left, right = map(str, input().split())
    if root not in tree_dic:
        tree_dic[root] = TreeNode(root)
    if left not in tree_dic and left != '.':
        tree_dic[left] = TreeNode(left)
    if right not in tree_dic and right != '.':
        tree_dic[right] = TreeNode(right)
    if left != '.':
        tree_dic[root].left = tree_dic[left]
    if right != '.':
        tree_dic[root].right = tree_dic[right]

def preorder(root):
    if root == None:
        return
    print(root.data, end="")
    preorder(root.left)
    preorder(root.right)

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.data, end="")
    inorder(root.right)

def postorder(root):
    if root == None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.data, end="")

preorder(tree_dic["A"])
print()
inorder(tree_dic["A"])
print()
postorder(tree_dic["A"])
print()
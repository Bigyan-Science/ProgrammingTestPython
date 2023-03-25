#Write code to print InOrder traversal of a tree?
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def in_order_traversal(root):
    if root:
        # Traverse the left subtree
        in_order_traversal(root.left)

        # Visit the node
        print(root.data, end=' ')

        # Traverse the right subtree
        in_order_traversal(root.right)

# Define the binary tree

def pre_order_traversal(root):
    if root:
        print(root.data,end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.data,end=' ')

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

print("In order traversal of tree")
in_order_traversal(root)
print()
print("Pre order traversal of tree")
pre_order_traversal(root)
print()
print("Post order traversal of tree")
post_order_traversal(root)

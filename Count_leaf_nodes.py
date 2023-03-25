class LeafNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


def count_leaf_nodes(root):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    return count_leaf_nodes(root.left) + count_leaf_nodes(root.right)


# Create the binary tree
root = LeafNode(1)
root.left = LeafNode(2)
root.right = LeafNode(3)
root.left.left = LeafNode(4)
root.left.right = LeafNode(5)
root.right.left = LeafNode(6)
root.right.right = LeafNode(7)

# Count the number of leaf nodes in the tree
number_of_leaf_nodes = count_leaf_nodes(root)
print("Number of leaf nodes: ", number_of_leaf_nodes)

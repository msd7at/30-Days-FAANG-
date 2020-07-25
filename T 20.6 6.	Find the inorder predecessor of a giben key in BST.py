# Data structure to store a Binary Search Tree node
class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# Recursive function to insert a key into BST
def insert(root, key):

    # if the root is None, create a node and return it
    if root is None:
        return Node(key)

    # if given key is less than the root node, recur for left subtree
    if key < root.data:
        root.left = insert(root.left, key)

    # if given key is more than the root node, recur for right subtree
    else:
        root.right = insert(root.right, key)

    return root


# Helper function to find maximum value node in given BST
def findMaximum(root):

    while root.right:
        root = root.right
    return root


# Recursive function to find in-order predecessor for given key in a BST
def findPredecessor(root, prec, key):

    # base case
    if root is None:
        return None

    # if node with key's value is found, the predecessor is maximum value
    # node in its left subtree (if any)
    if root.data == key:
        if root.left:
            return findMaximum(root.left)

    # if given key is less than the root node, recur for left subtree
    elif key < root.data:
        return findPredecessor(root.left, prec, key)

    # if given key is more than the root node, recur for right subtree
    else:
        # update predecessor to current node before recursing
        # in right subtree
        prec = root
        return findPredecessor(root.right, prec, key)

    return prec


if __name__ == '__main__':

    """ Construct below tree
              15
            /    \
           /      \
          10       20
         /  \     /  \
        /    \   /    \
       8     12 16    25
    """

    keys = [15, 10, 20, 8, 12, 16, 25]

    root = None
    for key in keys:
        root = insert(root, key)

    # find in-order predecessor for each key
    for key in keys:
        prec = findPredecessor(root, None, key)

        if prec:
            print("Predecessor of node", key, "is", prec.data)
        else:
            print("Predecessor doesn't exists for node", key)

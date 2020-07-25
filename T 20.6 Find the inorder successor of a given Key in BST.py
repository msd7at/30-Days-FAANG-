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


# Helper function to find minimum value node in given BST
def findMinimum(root):

    while root.left:
        root = root.left
    return root


# Recursive function to find inorder successor for given key in a BST
def findSuccessor(root, succ, key):

    # base case
    if root is None:
        return None

    # if node with key's value is found, the successor is minimum value
    # node in its right subtree (if any)
    if root.data == key:
        if root.right:
            return findMinimum(root.right)

    # if given key is less than the root node, recur for left subtree
    elif key < root.data:

        # update successor to current node before recursing in left subtree
        succ = root
        return findSuccessor(root.left, succ, key)

    # if given key is more than the root node, recur for right subtree
    else:
        return findSuccessor(root.right, succ, key)

    return succ


if __name__ == '__main__':

    ''' Construct below BST
              15
            /    \
           /      \
          10       20
         /  \     /  \
        /    \   /    \
       8     12 16    25
    '''

    keys = [15, 10, 20, 8, 12, 16, 25]

    root = None
    for key in keys:
        root = insert(root, key)

    # find in-order successor for each key
    for key in keys:
        prec = findSuccessor(root, None, key)

        if prec:
            print("Successor of node", key, "is", prec.data)
        else:
            print("No Successor exists for node", key)

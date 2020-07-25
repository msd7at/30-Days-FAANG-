# Python program to find ceil of a given value in BST 

# A Binary tree node 
class Node: 
	
	# Constructor to create a new node 
	def __init__(self, data): 
		self.key = data 
		self.left = None
		self.right = None

# Function to find ceil of a given input in BST. If input 
# is more than the max key in BST, return -1 
def ceil(root, inp): 
	
	# Base Case 
	if root == None: 
		return -1
	
	# We found equal key 
	if root.key == inp : 
		return root.key 
	
	# If root's key is smaller, ceil must be in right subtree 
	if root.key < inp: 
		return ceil(root.right, inp) 
	
	# Else, either left subtre or root has the ceil value 
	val = ceil(root.left, inp) 
	return val if val >= inp else root.key 

# Driver program to test above function 
root = Node(8) 

root.left = Node(4) 
root.right = Node(12) 

root.left.left = Node(2) 
root.left.right = Node(6) 

root.right.left = Node(10) 
root.right.right = Node(14) 

for i in range(16): 
	print "% d % d" %(i, ceil(root, i)) 

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 

# we can also do it by returing last element of every level
def rightViewUtil(root, level, max_level): 
      
    # Base Case
    if root is None: 
        return
      
    # If this is the last node of its level 
    if (max_level[0] < level): 
        print(root.data,end=" ")
        max_level[0] = level 
  
    # Recur for right subtree first, then left subtree 
    rightViewUtil(root.right, level+1, max_level) 
    rightViewUtil(root.left, level+1, max_level) 
  
def rightView(root): 
    max_level = [0] 
    rightViewUtil(root, 1, max_level) 

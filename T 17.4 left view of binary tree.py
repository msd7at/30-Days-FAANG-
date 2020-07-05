      
    # Base Case 
    if root is None: 
        return
  
    # If this is the first node of its level 
    if (max_level[0] < level): 
        print(root.data,end=" ") 
        max_level[0] = level 
  
    # Recur for left and right subtree 
    leftViewUtil(root.left, level + 1, max_level) 
    leftViewUtil(root.right, level + 1, max_level) 
  
  
# A wrapper over leftViewUtil() 
def LeftView(root): 
    max_level = [0] 
    leftViewUtil(root, 1, max_level) 

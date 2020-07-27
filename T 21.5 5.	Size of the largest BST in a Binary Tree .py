def largestBst(root):
    res, minVal, maxVal, isBST = largestBstHelper(root)
    return res

def largestBstHelper(root):
    if root is None:
        return 0, float("inf"), float("-inf"), True
    leftRes, minValLeft, maxValLeft, isLeftBST = largestBstHelper(root.left)
    rightRes, minValRight, maxValRight, isRightBST = largestBstHelper(root.right)
    if isLeftBST and isRightBST and root.data > maxValLeft and root.data < minValRight:
        if root.left == None:
            minValLeft = root.data
        if root.right == None:
            maxValRight = root.data
        return 1 + leftRes + rightRes, minValLeft, maxValRight, True
    else:
        return max(leftRes, rightRes), 0, 0, False
        

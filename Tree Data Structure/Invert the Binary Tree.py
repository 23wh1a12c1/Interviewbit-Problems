class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # @param A : root node of tree
    # @return the root node in the tree
    def invertTree(self, A):
        # Base case: if the tree is empty, return None
        if not A:
            return None
        
        # Swap the left and right children of the current node
        A.left, A.right = A.right, A.left
        
        # Recursively invert the left subtree
        self.invertTree(A.left)
        
        # Recursively invert the right subtree
        self.invertTree(A.right)
        
        # Return the root node after inversion
        return A

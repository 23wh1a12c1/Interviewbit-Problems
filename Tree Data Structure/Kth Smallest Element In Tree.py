# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        # Inorder traversal (iterative)
        stack = []
        curr = A
        count = 0

        while stack or curr:
            # Go left
            while curr:
                stack.append(curr)
                curr = curr.left
            
            # Visit node
            curr = stack.pop()
            count += 1
            if count == B:
                return curr.val   # kth element found
            
            # Go right
            curr = curr.right
        
        return -1  # Should not happen if input is valid

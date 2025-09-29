#####    PYTHON3



# Definition for a binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of list of integers
    def pathSum(self, A, B):
        result = []
        current_path = []

        def dfs(node, current_sum):
            # Base case: if node is None, stop
            if not node:
                return

            # Add current node's value to the path
            current_path.append(node.val)
            
            # Check if it's a leaf node and the sum matches
            if not node.left and not node.right and current_sum == node.val:
                result.append(list(current_path)) # Add a copy of the path
            
            # Recurse on left child
            dfs(node.left, current_sum - node.val)
            
            # Recurse on right child
            dfs(node.right, current_sum - node.val)
            
            # Backtrack: remove current node's value from the path
            current_path.pop()

        dfs(A, B)
        return result

# Example Usage:
# To test with the given example:
# tree = TreeNode(5)
# tree.left = TreeNode(4)
# tree.right = TreeNode(8)
# tree.left.left = TreeNode(11)
# tree.right.left = TreeNode(13)
# tree.right.right = TreeNode(4)
# tree.left.left.left = TreeNode(7)
# tree.left.left.right = TreeNode(2)
# tree.right.right.left = TreeNode(5)
# tree.right.right.right = TreeNode(1)

# sol = Solution()
# print(sol.pathSum(tree, 22))
# Expected output: [[5, 4, 11, 2], [5, 8, 4, 5]]

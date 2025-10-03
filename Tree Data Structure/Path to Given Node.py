# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        path = []
        # Helper function to perform DFS and find the path
        def find_path_dfs(node, target, current_path):
            if not node:
                return False

            current_path.append(node.val)

            if node.val == target:
                return True

            # Check left subtree
            if find_path_dfs(node.left, target, current_path):
                return True

            # Check right subtree
            if find_path_dfs(node.right, target, current_path):
                return True

            # If target not found in this subtree, backtrack
            current_path.pop()
            return False

        find_path_dfs(A, B, path)
        return path

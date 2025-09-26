# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return a list of integers
    def solve(self, A, B):
        if not A or A.val == B:
            return []

        queue = deque([A])

        while queue:
            level_size = len(queue)
            found_b_parent = False
            siblings = []
            cousins_on_level = []

            for _ in range(level_size):
                node = queue.popleft()

                # Check for cousins and siblings
                if node.left and node.left.val == B:
                    found_b_parent = True
                    if node.right:
                        siblings.append(node.right.val)
                elif node.right and node.right.val == B:
                    found_b_parent = True
                    if node.left:
                        siblings.append(node.left.val)
                else:
                    if node.left:
                        cousins_on_level.append(node.left.val)
                        queue.append(node.left)
                    if node.right:
                        cousins_on_level.append(node.right.val)
                        queue.append(node.right)

            if found_b_parent:
                # We have processed the entire level where B's children are.
                # All remaining nodes in the queue at this point belong to the next level,
                # which are B's cousins.
                
                # We need to collect the nodes from the children of the current level
                # that were not B's siblings.
                result = []
                for val in cousins_on_level:
                    if val not in siblings:
                         result.append(val)
                return result

        return []

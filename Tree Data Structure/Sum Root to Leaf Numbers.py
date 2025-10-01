###   PYTHON3


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumNumbers(self, A):
        MOD = 1003

        def dfs(node, curr):
            if not node:
                return 0

            curr = (curr * 10 + node.val) % MOD

            # if leaf node
            if not node.left and not node.right:
                return curr

            # recursive calls
            left_sum = dfs(node.left, curr)
            right_sum = dfs(node.right, curr)

            return (left_sum + right_sum) % MOD

        return dfs(A, 0)


#####   JAVA


/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

public class Solution {
    private static final int MOD = 1003;

    public int sumNumbers(TreeNode root) {
        return dfs(root, 0) % MOD;
    }

    private int dfs(TreeNode node, int curr) {
        if (node == null) return 0;

        curr = (curr * 10 + node.val) % MOD;

        // If it's a leaf node
        if (node.left == null && node.right == null) {
            return curr;
        }

        int leftSum = dfs(node.left, curr);
        int rightSum = dfs(node.right, curr);

        return (leftSum + rightSum) % MOD;
    }
}



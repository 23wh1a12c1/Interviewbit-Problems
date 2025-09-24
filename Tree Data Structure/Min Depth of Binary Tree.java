/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) {
 *         val = x;
 *         left = null;
 *         right = null;
 *     }
 * }
 */
public class Solution {
    public int minDepth(TreeNode root) {
        // Base case: If the root is null, the depth is 0.
        if (root == null) {
            return 0;
        }

        // If it's a leaf node, its depth is 1.
        if (root.left == null && root.right == null) {
            return 1;
        }

        // If only the left child exists, explore the left subtree.
        if (root.left != null && root.right == null) {
            return 1 + minDepth(root.left);
        }

        // If only the right child exists, explore the right subtree.
        if (root.left == null && root.right != null) {
            return 1 + minDepth(root.right);
        }

        // If both children exist, take the minimum depth of the subtrees and add 1 for the current node.
        return 1 + Math.min(minDepth(root.left), minDepth(root.right));
    }
}

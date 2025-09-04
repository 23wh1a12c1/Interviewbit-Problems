/**
 * Definition for binary tree
 * class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public TreeNode getSuccessor(TreeNode root, int b) {
        TreeNode successor = null;
        
        while (root != null) {
            if (b < root.val) {
                successor = root;   // possible successor
                root = root.left;   // try smaller values
            } else {
                root = root.right;  // need a bigger value
            }
        }
        
        return successor;
    }
}

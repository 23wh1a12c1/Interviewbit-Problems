####   JAVA8




/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

import java.util.Stack;

public class Solution {
    private Stack<TreeNode> stack = new Stack<>();

    // Constructor: push all left children
    public Solution(TreeNode root) {
        pushAllLeft(root);
    }

    /** @return whether we have a next smallest number */
    public boolean hasNext() {
        return !stack.isEmpty();
    }

    /** @return the next smallest number */
    public int next() {
        TreeNode node = stack.pop();
        int result = node.val;
        if (node.right != null) {
            pushAllLeft(node.right);
        }
        return result;
    }

    // Helper to push all left nodes into stack
    private void pushAllLeft(TreeNode node) {
        while (node != null) {
            stack.push(node);
            node = node.left;
        }
    }
}

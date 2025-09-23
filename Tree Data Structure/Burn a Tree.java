####    C++


#define t TreeNode*
int findDepth(t A,int B,int d)
{
    if(A==NULL) return 0;
    if(A->val==B) return d;
    return max(findDepth(A->left,B,d+1),findDepth(A->right,B,d+1));
}
int depth(t A)
{
    if(A==NULL) return 0;
    return 1+max(depth(A->right),depth(A->left));
}
int find(t A,int &mx,int B,int d)
{
    if(A==NULL) return 0;
    if(A->val==B) 
    {
         mx = max(mx,max(depth(A->right),depth(A->left)));
         return 1;
    }
    if(find(A->left,mx,B,d-1))
    {
        mx = max(mx,depth(A->right)+d);
        return 1;
    }
    if(find(A->right,mx,B,d-1))
    {
        mx = max(mx,depth(A->left)+d);
        return 1;
    }
    return 0;
}
int Solution::solve(TreeNode* A, int B) {
    int d = findDepth(A,B,0);
    int mx = 0;
    find(A,mx,B,d);
    return mx;
}



####   JAVA



/**
 * Definition for binary tree
 * public class TreeNode {
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

    private int findDepth(TreeNode root, int B, int d) {
        if (root == null) return -1;
        if (root.val == B) return d;
        int left = findDepth(root.left, B, d + 1);
        int right = findDepth(root.right, B, d + 1);
        return Math.max(left, right);
    }

    private int depth(TreeNode root) {
        if (root == null) return 0;
        return 1 + Math.max(depth(root.left), depth(root.right));
    }

    private boolean find(TreeNode root, int B, int d, int[] mx) {
        if (root == null) return false;
        if (root.val == B) {
            mx[0] = Math.max(mx[0], Math.max(depth(root.left), depth(root.right)));
            return true;
        }
        if (find(root.left, B, d - 1, mx)) {
            mx[0] = Math.max(mx[0], depth(root.right) + d);
            return true;
        }
        if (find(root.right, B, d - 1, mx)) {
            mx[0] = Math.max(mx[0], depth(root.left) + d);
            return true;
        }
        return false;
    }

    public int solve(TreeNode A, int B) {
        int d = findDepth(A, B, 0);
        int[] mx = new int[1]; // use array to pass by reference
        find(A, B, d, mx);
        return mx[0];
    }
}


















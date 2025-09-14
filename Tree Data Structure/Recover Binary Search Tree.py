####   PYTHON3



# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @return a list of integers
    def recoverTree(self, A):
        self.first = None
        self.second = None
        self.prev = None

        # Helper: inorder traversal
        def inorder(node):
            if not node:
                return
            inorder(node.left)

            if self.prev and node.val < self.prev.val:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node

            inorder(node.right)

        inorder(A)

        return sorted([self.first.val, self.second.val])








###   C++



/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

 void dfs(TreeNode* A, int& small, vector<int>& res) {
     if(A == NULL) return;
     dfs(A->left, small, res);
     if(small > A->val) {
         if(res.empty()) {
             res.push_back(small);
             res.push_back(A->val);
         } else res.back() = A->val;
     }
     small = A->val;
     dfs(A->right, small, res);
 }
vector<int> Solution::recoverTree(TreeNode* A) {
    vector<int> res;
    int small = INT_MIN;
    dfs(A,small,res);
    sort(begin(res),end(res));
    return res;
}



#####   JAVA



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
    TreeNode first, second, prev;

    public ArrayList<Integer> recoverTree(TreeNode A) {
        first = second = prev = null;
        inorder(A);

        ArrayList<Integer> result = new ArrayList<>();
        if (first != null && second != null) {
            result.add(Math.min(first.val, second.val));
            result.add(Math.max(first.val, second.val));
        }
        return result;
    }

    private void inorder(TreeNode root) {
        if (root == null) return;

        inorder(root.left);

        if (prev != null && root.val < prev.val) {
            if (first == null) {
                first = prev;
            }
            second = root;
        }
        prev = root;

        inorder(root.right);
    }
}





















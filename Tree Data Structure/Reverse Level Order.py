####   C++


/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
vector<int> Solution::solve(TreeNode* A) {
    vector<int> ans;
    queue<TreeNode*> q;
    if(A == NULL)
        return ans;
    q.push(A);
    while(!q.empty())
    {
        auto p = q.front();
        q.pop();
        ans.push_back(p->val);
        if(p->right)
            q.push(p->right);
        if(p->left)
            q.push(p->left);
    }
    reverse(ans.begin(),ans.end());
    return ans;
}



###   PYTHON3


from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def solve(self, A: TreeNode):
        ans = []
        if A is None:
            return ans
        q = deque([A])
        while q:
            node = q.popleft()
            ans.append(node.val)
            # Push right child first, then left child, 
            # so when reversed it becomes left to right bottom up traversal
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        ans.reverse()
        return ans




###   JAVA














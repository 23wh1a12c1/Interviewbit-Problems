####     C++





/**
 * Definition for binary tree with next pointer.
 * struct TreeLinkNode {
 *  int val;
 *  TreeLinkNode *left, *right, *next;
 *  TreeLinkNode(int x) : val(x), left(NULL), right(NULL), next(NULL) {}
 * };
 */
void Solution::connect(TreeLinkNode* A) {
    queue<TreeLinkNode*> Q;
    Q.push(A);
    while(!Q.empty()) {
        int sz = Q.size();
        while(sz--) {
            auto u = Q.front(); Q.pop();
            if(sz) u->next = Q.front();
            if(u->left) Q.push(u->left);
            if(u->right) Q.push(u->right);
        }
    }
}

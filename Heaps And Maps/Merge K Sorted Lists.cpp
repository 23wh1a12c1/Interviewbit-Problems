###    C++



/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
ListNode* Solution::mergeKLists(vector<ListNode*> &A) {
    ListNode* dummy = new ListNode(-1);
    priority_queue<pair<int,ListNode*>,vector<pair<int,ListNode*>>, greater<pair<int,ListNode*>>> Q;
    for(auto& a : A) Q.push({a->val, a});
    
    ListNode* runner = dummy;
    while(!Q.empty()) {
        auto [_, node] = Q.top(); Q.pop();
        runner->next = node;
        runner = runner->next;
        if(node->next != NULL) Q.push({node->next->val, node->next});
        runner->next = NULL;
    }
    
    return dummy->next;
}




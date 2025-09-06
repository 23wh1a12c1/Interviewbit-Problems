####   PYTHON3

# Definition for a binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @return an integer
    def t2Sum(self, A, B):
        if not A:
            return 0

        # Stacks for inorder and reverse inorder traversals
        s1, s2 = [], []

        # Initialize iterators
        curr1, curr2 = A, A

        while curr1:
            s1.append(curr1)
            curr1 = curr1.left

        while curr2:
            s2.append(curr2)
            curr2 = curr2.right

        n1 = s1[-1] if s1 else None
        n2 = s2[-1] if s2 else None

        while n1 and n2 and n1.val < n2.val:
            total = n1.val + n2.val
            if total == B:
                return 1
            elif total < B:
                # Move inorder iterator forward
                temp = s1.pop()
                temp = temp.right
                while temp:
                    s1.append(temp)
                    temp = temp.left
                n1 = s1[-1] if s1 else None
            else:
                # Move reverse inorder iterator backward
                temp = s2.pop()
                temp = temp.left
                while temp:
                    s2.append(temp)
                    temp = temp.right
                n2 = s2[-1] if s2 else None

        return 0










###     JAVA



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

import java.util.*;

public class Solution {
    public int t2Sum(TreeNode A, int B) {
        if (A == null) return 0;

        Stack<TreeNode> s1 = new Stack<>(); // inorder (ascending)
        Stack<TreeNode> s2 = new Stack<>(); // reverse inorder (descending)

        TreeNode curr1 = A, curr2 = A;

        // initialize stacks
        while (curr1 != null) {
            s1.push(curr1);
            curr1 = curr1.left;
        }
        while (curr2 != null) {
            s2.push(curr2);
            curr2 = curr2.right;
        }

        TreeNode n1 = s1.peek();
        TreeNode n2 = s2.peek();

        while (n1 != null && n2 != null && n1.val < n2.val) {
            int sum = n1.val + n2.val;

            if (sum == B) return 1;
            else if (sum < B) {
                // move inorder iterator forward
                TreeNode temp = s1.pop();
                temp = temp.right;
                while (temp != null) {
                    s1.push(temp);
                    temp = temp.left;
                }
                n1 = s1.isEmpty() ? null : s1.peek();
            } else {
                // move reverse inorder iterator backward
                TreeNode temp = s2.pop();
                temp = temp.left;
                while (temp != null) {
                    s2.push(temp);
                    temp = temp.right;
                }
                n2 = s2.isEmpty() ? null : s2.peek();
            }
        }
        return 0;
    }
}





###   C++



// https://www.interviewbit.com/problems/2-sum-binary-tree/

/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
// A shorter and intuitive method. Check out the next two solutions as well.
int Solution::t2Sum(TreeNode* A, int B) {
    // Base Case
    if(!A)return 0;
    
    // Make two stacks for the two different traversals,
    // one from the right side, other from the left.
    stack<TreeNode*> s1, s2;
    TreeNode* temp1 = A, *temp2 = A;
    
    // Take temp1 to the extreme left
    while(temp1){
        s1.push(temp1);
        temp1 = temp1->left;
    }
    
    // and temp2 to extreme right
    while(temp2){
        s2.push(temp2);
        temp2 = temp2->right;
    }
    temp1 = s1.top();
    temp2 = s2.top();
    
    // While we do not traverse the complete tree
    while(temp1 and temp2 and temp1->val < temp2 -> val){
        if(temp1->val + temp2->val == B)return 1;

        if(temp1->val + temp2->val < B){
            // Move Ahead the temp1 pointer
            s1.pop();
            // Check out the preorder traversal using stacks 
            temp1 = temp1->right;
            while(temp1){
                s1.push(temp1);
                temp1 = temp1->left;
            }
            temp1 = s1.top();
        }else{
            // Move ahead the temp2 pointer
            s2.pop();
            // Inverse of preorder traversal using stacks 
            // (not to be confused with postorder traversal)
            temp2 = temp2->left;
            while(temp2){
                s2.push(temp2);
                temp2 = temp2->right;
            }
            temp2 = s2.top();
        }
    }
    return 0;
}


// int Solution::t2Sum(TreeNode* A, int B) {
    
//     stack<TreeNode*> st1;
//     stack<TreeNode*> st2;
    
//     int val1 = 0, val2 = 0;
//     int done1 = 0, done2 = 0;
    
//     TreeNode* curr1 = A;
//     TreeNode* curr2 = A;
    
    
//     while(1){
//         while(done1 == 0){
//             if(curr1 != NULL){
//                 st1.push(curr1);
//                 curr1 = curr1->left;
//             }
//             else{
//                 if(st1.empty()){
//                     done1 = 1;
//                 }
//                 else{
//                     curr1 = st1.top();
//                     val1 = curr1->val;
//                     st1.pop();
//                     curr1 = curr1->right;
//                     done1 = 1;    
//                 }
//             }
//         }
        
//         while(done2 == 0){
//             if(curr2 != NULL){
//                 st2.push(curr2);
//                 curr2 = curr2->right;
//             }
//             else{
//                 if(st2.empty()){
//                     done2 = 1;
//                 }
//                 else{
//                     curr2 = st2.top();
//                     st2.pop();
//                     val2 = curr2->val;
//                     curr2 = curr2->left;
//                     done2 = 1;
//                 }
//             }
//         }
        
//         if(((val1 + val2) == B) && (val1 != val2)){
//             return 1;
//         }
//         else if((val1 + val2) < B){
//             done1 = 0;
//         }
//         else if((val1 + val2) > B){
//             done2 = 0;
//         }
        
//         if(val1 >= val2){
//             return 0;
//         }
//     }
    
//     return 0;
// }

/*
Another method if you are unable to get above method, although both of them work the same.
*/


// bool isPairPresent(int K, TreeNode* A, TreeNode* B, stack<TreeNode*> s1, stack<TreeNode*> s2){
//     // Base Case
//     if(!A)return 0;

//     // Go to the extreme left
//     while(A){
//         s1.push(A);
//         A = A ->left;
//     }
//     // Go to the extreme right
//     while(B){
//         s2.push(B);
//         B = B->right;
//     }

//     Get the lowest and highest elements.
//     A = s1.top(); s1.pop();
//     B = s2.top(); s2.pop();
    
//     // Make the extremes as lowest and highest values (coz BST)
//     int low = A->val, high = B->val;
//     bool b1 = true;
//     bool b2 = true;
//     // While we don't cross the two pointers
//     while(low < high){
//         // Return if we have found the sum
//         if(low + high == K)return 1;
//         // If the sum is less, increase the lower pointer only.
//         if(low + high < K){
//             b2 = false;
//             b1 = true;
//         }
//         // Else decrement the higher pointer only.
//         else {
//             b2 = true;
//             b1 = false;
//         }
//         if(b1){
//             // If the pointer is not NULL, take it to the extreme left
//             // of its right child
//             if(A){
//                 A = A->right;
//                 while(A){
//                     s1.push(A);
//                     A = A->left;
//                 }
//             }
//             // Else just pop the top of the stack and make it as the lowest pointer.
//             else {
//                 A = s1.top();
//                 s1.pop();
//                 low = A->val;
//             }
//         }
//         // Same as above.
//         else if(b2){
            
//             if(B){
//                 B = B->left;
//                 while(B){
//                     s2.push(B);
//                     B = B->right;
//                 }
//             }else {
//                 B = s2.top();
//                 s2.pop();
//                 high = B->val;
//             }
//         }
//     }
//     return 0;
// }

// int Solution::t2Sum(TreeNode* A, int B) {
//     stack<TreeNode*> s1, s2;

//     TreeNode *head1 = A, *head2 = A;
    
//     return isPairPresent(B, head1, head2, s1, s2);
// }

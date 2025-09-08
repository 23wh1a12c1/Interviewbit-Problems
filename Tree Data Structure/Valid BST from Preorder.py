###   PYTHON3


class Solution:
    def solve(self, A):
        stack = []
        lower_bound = float('-inf')
        
        for val in A:
            # Check duplicates and lower bound
            if val <= lower_bound:
                return 0
            
            # Move to the right subtree and update lower bound
            while stack and val > stack[-1]:
                lower_bound = stack.pop()
            
            # Check duplicates in stack top
            if stack and stack[-1] == val:
                return 0
            
            stack.append(val)
        
        return 1



###  JAVA


import java.util.ArrayList;
import java.util.Stack;

public class Solution {
    public int solve(ArrayList<Integer> A) {
        Stack<Integer> stack = new Stack<>();
        int lowerBound = Integer.MIN_VALUE;
        
        for (int val : A) {
            // Check if val violates the lower bound constraint
            if (val <= lowerBound) {
                return 0;
            }
            
            // Pop elements smaller than current val and update lowerBound
            while (!stack.isEmpty() && val > stack.peek()) {
                lowerBound = stack.pop();
            }
            
            // Check for duplicates
            if (!stack.isEmpty() && stack.peek() == val) {
                return 0;
            }
            
            stack.push(val);
        }
        
        return 1;  // Valid BST preorder
    }
}




###   C++


int Solution::solve(vector<int> &A) {
    stack<int> st;
    int lowerBound = INT_MIN;

    for (int val : A) {
        // If current value is less than or equal to lowerBound, invalid BST preorder
        if (val <= lowerBound) {
            return 0;
        }

        // Pop all smaller elements and update lowerBound
        while (!st.empty() && val > st.top()) {
            lowerBound = st.top();
            st.pop();
        }

        // Check for duplicates
        if (!st.empty() && st.top() == val) {
            return 0;
        }

        st.push(val);
    }

    return 1;  // Valid preorder traversal of BST
}








####    C++


int Solution::solve(vector<int> &A, int B) {  
    int ans = 0;
    priority_queue<int> pq;
    for(int i = 0; i<A.size(); i++){
        pq.push(A[i]);
    }
    
    for(int i = 0; i<B; i++){
        int t = pq.top();
        ans += t;   
        pq.pop();
        pq.push(t-1);
    }
    return ans;
}


####  PYTHON3


import heapq

class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        max_heap = [-x for x in A]  # Negate all to simulate max-heap
        heapq.heapify(max_heap)

        ans = 0
        for _ in range(B):
            t = -heapq.heappop(max_heap)  # Get max (by negating back)
            ans += t
            heapq.heappush(max_heap, -(t - 1))  # Push decremented back (negated)

        return ans





#####    JAVA
import java.util.ArrayList;
import java.util.Collections;
import java.util.PriorityQueue;

public class Solution {
    public int solve(ArrayList<Integer> A, int B) {
        int ans = 0;

        // Max-heap using reverse order comparator
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());

        // Add all elements from A into the max-heap
        for (int num : A) {
            pq.add(num);
        }

        // Perform B operations
        for (int i = 0; i < B; i++) {
            int maxVal = pq.poll();  // Extract max
            ans += maxVal;
            pq.add(maxVal - 1);      // Push back after decrement
        }

        return ans;
    }
}






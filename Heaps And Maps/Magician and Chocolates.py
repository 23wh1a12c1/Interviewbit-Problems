####    C++



int check(priority_queue<int>& q, int& A){
    int ans = 0, divi = pow(10, 9) + 7;
    
    while(A){
        int top = q.top();
        
        ans = (ans + (top%divi))%divi;
        
        q.pop();
        q.push(top/2);
        
        A--;
    }
    
    return ans;
}

int Solution::nchoc(int A, vector<int> &B) {
    priority_queue<int> q;
    
    if(B.size() == 0){
        return 0;
    }
    
    for(int i = 0; i < B.size(); i++){
        q.push(B[i]);
    }

    return check(q, A);
}





#####    PYTHON3



import heapq

class Solution:
    # @param A : integer (minutes)
    # @param B : list of integers (chocolate bags)
    # @return an integer
    def nchoc(self, A, B):
        mod = 10**9 + 7
        
        # Python has a min-heap by default, so we simulate a max-heap using negative values
        max_heap = [-b for b in B]
        heapq.heapify(max_heap)
        
        total_chocolates = 0
        
        for _ in range(A):
            max_choco = -heapq.heappop(max_heap)
            total_chocolates = (total_chocolates + max_choco) % mod
            heapq.heappush(max_heap, -(max_choco // 2))
        
        return total_chocolates




#####    JAVA



import java.util.*;

public class Solution {
    public int nchoc(int A, ArrayList<Integer> B) {
        // Define modulo
        int mod = 1000000007;
        
        // Create a max-heap by using a PriorityQueue with reversed comparator
        PriorityQueue<Integer> maxHeap = new PriorityQueue<>(Collections.reverseOrder());
        
        // Add all elements to the maxHeap
        for (int chocolates : B) {
            maxHeap.add(chocolates);
        }
        
        long totalChocolates = 0; // Use long to avoid overflow during addition
        
        for (int i = 0; i < A; i++) {
            if (maxHeap.isEmpty()) {
                break; // no more chocolates left
            }
            
            int maxChoco = maxHeap.poll(); // get the max chocolates bag
            
            totalChocolates = (totalChocolates + maxChoco) % mod;
            
            // Put back half the chocolates (integer division)
            maxHeap.offer(maxChoco / 2);
        }
        
        return (int) totalChocolates;
    }
}



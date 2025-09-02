### PYTHON3


import heapq

class Solution:
    # A, B: lists of integers
    # C: integer
    # return: list of integers
    def solve(self, A, B, C):
        n = len(A)
        # Sort descending
        A.sort(reverse=True)
        B.sort(reverse=True)
        
        # Max heap: Python has min heap, so use negative sums
        max_heap = []
        # Push initial combination (sum, i, j)
        heapq.heappush(max_heap, (-(A[0] + B[0]), 0, 0))
        
        seen = set((0, 0))
        result = []
        
        while C > 0 and max_heap:
            neg_sum, i, j = heapq.heappop(max_heap)
            result.append(-neg_sum)
            
            if i + 1 < n and (i + 1, j) not in seen:
                heapq.heappush(max_heap, (-(A[i+1] + B[j]), i + 1, j))
                seen.add((i + 1, j))
            
            if j + 1 < n and (i, j + 1) not in seen:
                heapq.heappush(max_heap, (-(A[i] + B[j+1]), i, j + 1))
                seen.add((i, j + 1))
            
            C -= 1
        
        return result







####   JAVA


import java.util.*;

public class Solution {
    public ArrayList<Integer> solve(ArrayList<Integer> A, ArrayList<Integer> B, int C) {
        Collections.sort(A, Collections.reverseOrder());
        Collections.sort(B, Collections.reverseOrder());
        
        int n = A.size();
        ArrayList<Integer> result = new ArrayList<>();
        
        PriorityQueue<PairSum> maxHeap = new PriorityQueue<>();
        Set<String> seen = new HashSet<>();
        
        // Initial max sum (A[0] + B[0])
        maxHeap.offer(new PairSum(A.get(0) + B.get(0), 0, 0));
        seen.add("0#0");
        
        while (C-- > 0 && !maxHeap.isEmpty()) {
            PairSum current = maxHeap.poll();
            result.add(current.sum);
            
            int i = current.i;
            int j = current.j;
            
            if (i + 1 < n) {
                String key1 = (i + 1) + "#" + j;
                if (!seen.contains(key1)) {
                    maxHeap.offer(new PairSum(A.get(i + 1) + B.get(j), i + 1, j));
                    seen.add(key1);
                }
            }
            
            if (j + 1 < n) {
                String key2 = i + "#" + (j + 1);
                if (!seen.contains(key2)) {
                    maxHeap.offer(new PairSum(A.get(i) + B.get(j + 1), i, j + 1));
                    seen.add(key2);
                }
            }
        }
        
        return result;
    }
    
    class PairSum implements Comparable<PairSum> {
        int sum;
        int i, j;
        
        PairSum(int sum, int i, int j) {
            this.sum = sum;
            this.i = i;
            this.j = j;
        }
        
        @Override
        public int compareTo(PairSum other) {
            return Integer.compare(other.sum, this.sum); // Max-heap behavior
        }
    }
}

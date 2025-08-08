####     C++


vector<int> Solution::solve(vector<vector<int> > &A) {
    priority_queue<array<int,3>, vector<array<int,3>>, greater<array<int,3>>> q;
    for(int i = 0; i < A.size(); i++) q.push({A[i][0], i, 0});
    vector<int> res;
    while(q.size()) {
        auto [v,r,c] = q.top(); q.pop();
        res.push_back(v);
        if(A[r].size() != c + 1) q.push({A[r][c+1],r,c+1});
    }
    
    return res;
}



###   JAVA


import java.util.*;

public class Solution {
    public ArrayList<Integer> solve(ArrayList<ArrayList<Integer>> A) {
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        ArrayList<Integer> res = new ArrayList<>();

        // Initialize heap with first element of each row
        for (int i = 0; i < A.size(); i++) {
            if (!A.get(i).isEmpty()) {
                pq.offer(new int[]{A.get(i).get(0), i, 0});  // {value, row, col}
            }
        }

        // Merge all sorted rows
        while (!pq.isEmpty()) {
            int[] curr = pq.poll();
            int val = curr[0], row = curr[1], col = curr[2];
            res.add(val);

            if (col + 1 < A.get(row).size()) {
                pq.offer(new int[]{A.get(row).get(col + 1), row, col + 1});
            }
        }

        return res;
    }
}




####    PYTHON3


import heapq

class Solution:
    # @param A : list of list of integers
    # @return a list of integers
    def solve(self, A):
        res = []
        heap = []

        # Push the first element of each list into the heap
        for i in range(len(A)):
            if A[i]:
                heapq.heappush(heap, (A[i][0], i, 0))  # (value, row, column)

        # Process the heap
        while heap:
            val, r, c = heapq.heappop(heap)
            res.append(val)

            # Push next element from the same row if exists
            if c + 1 < len(A[r]):
                heapq.heappush(heap, (A[r][c + 1], r, c + 1))

        return res










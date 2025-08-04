import heapq

class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        if len(A) <= 1:
            return 0

        heapq.heapify(A)  # convert list to min-heap
        total_cost = 0

        while len(A) > 1:
            first = heapq.heappop(A)
            second = heapq.heappop(A)
            cost = first + second
            total_cost += cost
            heapq.heappush(A, cost)

        return total_cost

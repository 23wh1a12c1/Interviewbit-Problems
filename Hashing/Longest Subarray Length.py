class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        # Convert 0 to -1 to transform the problem into a prefix sum problem
        prefix_sum = 0
        max_len = 0

        # Dictionary to store the first occurrence of a prefix_sum
        prefix_index = {}

        for i in range(len(A)):
            if A[i] == 1:
                prefix_sum += 1
            else:
                prefix_sum -= 1

            # If prefix_sum == 1, entire subarray from 0 to i is valid
            if prefix_sum == 1:
                max_len = i + 1

            # If (prefix_sum - 1) seen before, then subarray from that index+1 to i has sum == 1
            if (prefix_sum - 1) in prefix_index:
                max_len = max(max_len, i - prefix_index[prefix_sum - 1])

            # Store first occurrence of each prefix_sum
            if prefix_sum not in prefix_index:
                prefix_index[prefix_sum] = i

        return max_len

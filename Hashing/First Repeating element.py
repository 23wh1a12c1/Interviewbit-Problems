class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        index_map = {}
        repeating = set()
        
        for i, num in enumerate(A):
            if num in index_map:
                repeating.add(num)
            else:
                index_map[num] = i

        min_index = float('inf')
        result = -1

        for num in repeating:
            if index_map[num] < min_index:
                min_index = index_map[num]
                result = num

        return result

# PYTHON3


class Solution:
    # @param A : integer
    # @return a list of integers
    def grayCode(self, A):
        result = []
        for i in range(1 << A):  # Loop from 0 to 2^A - 1
            gray = i ^ (i >> 1)
            result.append(gray)
        return result

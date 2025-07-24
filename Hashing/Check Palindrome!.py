#######   PYTHON3



class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        freq = [0] * 26

        for ch in A:
            freq[ord(ch) - ord('a')] += 1

        odd_count = 0
        for count in freq:
            if count % 2 == 1:
                odd_count += 1

        if odd_count > 1:
            return 0
        return 1

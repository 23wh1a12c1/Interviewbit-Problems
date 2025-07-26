
###   PYTHON3


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        from collections import defaultdict

        count = defaultdict(int)
        count[0] = 1  # Base case: zero odd numbers before starting
        odd_count = 0
        result = 0

        for num in A:
            if num % 2 == 1:
                odd_count += 1
            if odd_count - B in count:
                result += count[odd_count - B]
            count[odd_count] += 1

        return result


#### JAVA


import java.util.*;

public class Solution {
    public int solve(ArrayList<Integer> A, int B) {
        Map<Integer, Integer> count = new HashMap<>();
        count.put(0, 1);  // Base case: 0 odd numbers seen initially

        int oddCount = 0;
        int result = 0;

        for (int num : A) {
            if (num % 2 != 0) {
                oddCount++;
            }

            result += count.getOrDefault(oddCount - B, 0);
            count.put(oddCount, count.getOrDefault(oddCount, 0) + 1);
        }

        return result;
    }
}

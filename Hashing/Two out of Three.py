# JAVA





  import java.util.*;

public class Solution {
    public ArrayList<Integer> solve(ArrayList<Integer> A, ArrayList<Integer> B, ArrayList<Integer> C) {
        // Use a HashSet to eliminate duplicates within the same array
        Set<Integer> setA = new HashSet<>(A);
        Set<Integer> setB = new HashSet<>(B);
        Set<Integer> setC = new HashSet<>(C);

        // Map to count how many arrays each number appears in
        HashMap<Integer, Integer> map = new HashMap<>();

        for (int num : setA) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        for (int num : setB) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        for (int num : setC) {
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        // Collect elements that appeared in at least 2 arrays
        ArrayList<Integer> result = new ArrayList<>();
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue() >= 2) {
                result.add(entry.getKey());
            }
        }

        // Sort the result
        Collections.sort(result);
        return result;
    }
}







# PYTHON3






  class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @param C : list of integers
    # @return a list of integers
    def solve(self, A, B, C):
        from collections import defaultdict

        # Use sets to avoid duplicate values from the same list
        setA = set(A)
        setB = set(B)
        setC = set(C)

        count_map = defaultdict(int)

        for num in setA:
            count_map[num] += 1
        for num in setB:
            count_map[num] += 1
        for num in setC:
            count_map[num] += 1

        result = [num for num, count in count_map.items() if count >= 2]
        return sorted(result)

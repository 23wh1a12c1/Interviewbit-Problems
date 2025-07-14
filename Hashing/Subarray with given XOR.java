import java.util.*;

public class Solution {
    public int solve(ArrayList<Integer> A, int B) {
        HashMap<Integer, Integer> freqMap = new HashMap<>();
        int prefixXOR = 0;
        int count = 0;

        for (int num : A) {
            prefixXOR ^= num;

            if (prefixXOR == B) {
                count++;
            }

            int y = prefixXOR ^ B;
            if (freqMap.containsKey(y)) {
                count += freqMap.get(y);
            }

            freqMap.put(prefixXOR, freqMap.getOrDefault(prefixXOR, 0) + 1);
        }

        return count;
    }
}

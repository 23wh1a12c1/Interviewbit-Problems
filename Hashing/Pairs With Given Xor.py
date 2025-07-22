###########           C++




int Solution::solve(vector<int> &A, int B) {
    int res = 0;
    unordered_map<int, int> freq;
    for(auto a : A) {
        res += freq[a^B];
        freq[a]++;
    }
    return res;
}




# PYTHON3




class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        res = 0
        freq = {}
        
        for a in A:
            res += freq.get(a ^ B, 0)
            freq[a] = freq.get(a, 0) + 1
        
        return res







###############            JAVA




import java.util.*;

public class Solution {
    public int solve(ArrayList<Integer> A, int B) {
        int res = 0;
        HashMap<Integer, Integer> freq = new HashMap<>();

        for (int a : A) {
            res += freq.getOrDefault(a ^ B, 0);
            freq.put(a, freq.getOrDefault(a, 0) + 1);
        }

        return res;
    }
}















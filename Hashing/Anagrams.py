#   C++




vector<vector<int> > Solution::anagrams(const vector<string> &A) {
    vector<vector<int> > sol;
    unordered_map<string, vector<int> > myMap;
    string temp;
    for(int i = 0; i < A.size(); i++){
        temp = A[i];
        sort(temp.begin(),temp.end());
        myMap[temp].push_back(i+1);
    }
    
    auto it = myMap.begin();
    
    while(it != myMap.end()){
        sol.push_back(it->second);
        it++;
    }

    return sol;
}






# JAVA



import java.util.*;

public class Solution {
    // DO NOT MODIFY THE LIST. IT IS READ ONLY
    public ArrayList<ArrayList<Integer>> anagrams(final List<String> A) {
        HashMap<String, ArrayList<Integer>> map = new HashMap<>();
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();

        for (int i = 0; i < A.size(); i++) {
            String str = A.get(i);
            char[] chars = str.toCharArray();
            Arrays.sort(chars);  // Sort to group anagrams
            String key = new String(chars);

            // Add index (i + 1 for 1-based indexing)
            map.computeIfAbsent(key, k -> new ArrayList<>()).add(i + 1);
        }

        // Collect grouped anagram indices
        for (ArrayList<Integer> group : map.values()) {
            result.add(group);
        }

        return result;
    }
}




# PYTHON3



class Solution:
    # @param A : tuple of strings
    # @return a list of list of integers
    def anagrams(self, A):
        from collections import defaultdict

        anagram_map = defaultdict(list)
        
        for i, word in enumerate(A):
            key = ''.join(sorted(word))
            anagram_map[key].append(i + 1)  # 1-based indexing

        return list(anagram_map.values())








































###    C++



/*
Given a string, 
find the length of the longest substring without repeating characters.

Example:

The longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3.

For "bbbbb" the longest substring is "b", with the length of 1.

https://www.interviewbit.com/problems/longest-substring-without-repeat/
*/

int Solution::lengthOfLongestSubstring(string A) {
    if (A.empty())
        return 0;
    
    unordered_map<char, int> ls;
    int count = 0;
    int ans = 0;
    
    auto q = 0;
    auto size = A.size();
    
    while (q<size)
    {
        if (ls.find(A[q]) == ls.end())
        {
            ls[A[q]] = q;
            ++count; ++q;
        }
        else
        {
            q = ls[A[q]] + 1;
            ls.clear();
            ans = max(count, ans);
            count = 0;
        }
    }
    ans = max(count, ans);
    
    return ans;
}





###   PYTHON3


class Solution:
    # @param A : string
    # @return an integer
    def lengthOfLongestSubstring(self, A):
        if not A:
            return 0
        
        seen = {}
        left = 0
        max_len = 0

        for right in range(len(A)):
            char = A[right]

            if char in seen and seen[char] >= left:
                left = seen[char] + 1  # Move left to right of previous duplicate

            seen[char] = right  # Update the last seen index of char
            max_len = max(max_len, right - left + 1)

        return max_len






#####   JAVA



public class Solution {
    public int lengthOfLongestSubstring(String A) {
        if (A == null || A.length() == 0) {
            return 0;
        }

        Map<Character, Integer> seen = new HashMap<>();
        int maxLen = 0;
        int left = 0;

        for (int right = 0; right < A.length(); right++) {
            char currentChar = A.charAt(right);

            if (seen.containsKey(currentChar) && seen.get(currentChar) >= left) {
                // Move left pointer to the right of last occurrence
                left = seen.get(currentChar) + 1;
            }

            // Update or add the current character index
            seen.put(currentChar, right);
            maxLen = Math.max(maxLen, right - left + 1);
        }

        return maxLen;
    }
}

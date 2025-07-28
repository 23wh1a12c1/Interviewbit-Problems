##########   C++


/*
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in linear time complexity.
Note that when the count of a character C in T is N, then the count of C in minimum window in S should be atleast N.

Example :

S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC"

 Note:
If there is no such window in S that covers all characters in T, return the empty string ''.
If there are multiple such windows, return the first occurring minimum window ( with minimum start index ).

https://www.interviewbit.com/problems/window-string/
*/

string Solution::minWindow(string S, string T) {
    auto sizeS = S.length();
    auto sizeT = T.length();
    
    if (sizeS < sizeT)
        return "";
        
    int needToFind[256] = {0};
    int hasFound[256] = {0};
    int count = 0;
    int minLength = INT_MAX;
    string res = ""; 
    
    for (auto i = 0; i<sizeT; ++i)
        needToFind[T[i]]++;
    
    for (int p = 0, q = 0; q<sizeS; ++q)
    {
        if (needToFind[S[q]] == 0)
            continue;
        
        hasFound[S[q]]++;
        
        if (hasFound[S[q]] <= needToFind[S[q]])
            ++count;
        
        if (count == sizeT)
        {
            while (hasFound[S[p]] == 0 || hasFound[S[p]] > needToFind[S[p]])
            {
                if (hasFound[S[p]] > needToFind[S[p]])
                    hasFound[S[p]]--;
                ++p;
            }
            
            auto currLength = q - p + 1; 
            if (currLength < minLength)
            {
                res.clear();
                res.append(S.begin()+p, S.begin()+q+1);
                minLength = currLength;
            }
        }
    }
    
    return res;
}



########   JAVA 



public class Solution {
    public String minWindow(String A, String B) {
        if (A.length() < B.length()) return "";

        int[] needToFind = new int[256];
        int[] hasFound = new int[256];

        for (char c : B.toCharArray()) {
            needToFind[c]++;
        }

        int minLen = Integer.MAX_VALUE;
        int count = 0, start = 0;
        int minStart = 0;

        for (int end = 0; end < A.length(); end++) {
            char c = A.charAt(end);
            if (needToFind[c] == 0) continue;

            hasFound[c]++;
            if (hasFound[c] <= needToFind[c]) {
                count++;
            }

            if (count == B.length()) {
                // Move start to the right as far as possible
                while (needToFind[A.charAt(start)] == 0 || hasFound[A.charAt(start)] > needToFind[A.charAt(start)]) {
                    if (hasFound[A.charAt(start)] > needToFind[A.charAt(start)]) {
                        hasFound[A.charAt(start)]--;
                    }
                    start++;
                }

                if (end - start + 1 < minLen) {
                    minLen = end - start + 1;
                    minStart = start;
                }
            }
        }

        return (minLen == Integer.MAX_VALUE) ? "" : A.substring(minStart, minStart + minLen);
    }
}

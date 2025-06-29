# CPP


/*
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.



The digit 0 maps to 0 itself.
The digit 1 maps to 1 itself.

Input: Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Make sure the returned strings are lexicographically sorted.

https://www.interviewbit.com/problems/letter-phone/
*/

string temp = "";
unordered_map<char, string> keypad = {
    { '1', "1" },
    { '2', "abc" },
    { '3', "def" },
    { '4', "ghi" },
    { '5', "jkl" },
    { '6', "mno" },
    { '7', "pqrs" },
    { '8', "tuv" },
    { '9', "wxyz" },
    { '0', "0" }
};
void backtracking(string digits, int i, vector<string>& res)
{
    if (digits[i] - '0' > -1 && digits[i] - '0' < 10)
    {    
        string str = keypad[digits[i]];
        for (auto j = 0; j<str.length(); ++j)
        {
            temp += str[j]; 
            if (i == digits.length() - 1)
                res.emplace_back(temp);
            else
                backtracking(digits, i+1, res);
            temp.pop_back(); 
        }
    }
}
vector<string> Solution::letterCombinations(string A) {
    vector<string> res;
    backtracking(A, 0, res);
    return res;
}




# PYTHON3


class Solution:
    def letterCombinations(self, A):
        if not A:
            return []

        # Keypad mapping
        keypad = {
            '0': '0',
            '1': '1',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = []

        def backtrack(index, path):
            if index == len(A):
                result.append(path)
                return
            letters = keypad[A[index]]
            for letter in letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        result.sort()  # ensure lexicographic order
        return result





# JAVA


public class Solution {
    private static final String[] KEYPAD = {
        "0",    // 0
        "1",    // 1
        "abc",  // 2
        "def",  // 3
        "ghi",  // 4
        "jkl",  // 5
        "mno",  // 6
        "pqrs", // 7
        "tuv",  // 8
        "wxyz"  // 9
    };

    public ArrayList<String> letterCombinations(String A) {
        ArrayList<String> result = new ArrayList<>();
        if (A == null || A.length() == 0) return result;

        backtrack(A, 0, new StringBuilder(), result);
        Collections.sort(result); // Ensure lexicographical order
        return result;
    }

    private void backtrack(String digits, int index, StringBuilder path, ArrayList<String> result) {
        if (index == digits.length()) {
            result.add(path.toString());
            return;
        }

        char digit = digits.charAt(index);
        String letters = KEYPAD[digit - '0'];

        for (int i = 0; i < letters.length(); i++) {
            path.append(letters.charAt(i));
            backtrack(digits, index + 1, path, result);
            path.deleteCharAt(path.length() - 1); // backtrack
        }
    }
}

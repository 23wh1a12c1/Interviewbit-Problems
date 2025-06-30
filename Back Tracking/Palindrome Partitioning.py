# PYTHON3


class Solution:
    # @param A : string
    # @return a list of list of strings
    def partition(self, A):
        res = []
        
        # Helper to check if a string is palindrome
        def is_palindrome(s):
            return s == s[::-1]
        
        # Backtracking function
        def backtrack(start, path):
            if start == len(A):
                res.append(path[:])
                return
            for end in range(start + 1, len(A) + 1):
                substring = A[start:end]
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    path.pop()
        
        backtrack(0, [])

        # Sort the result based on the lexicographical rule
        def custom_sort_key(entry):
            return [len(part) for part in entry]

        res.sort(key=custom_sort_key)
        return res



# PYTHON3

class Solution:
    # @param A : integer (n)
    # @param B : integer (k)
    # @return a strings
    def getPermutation(self, A, B):
        import math

        nums = list(range(1, A + 1))
        B -= 1  # Convert to 0-based index
        fact = [1] * (A + 1)

        # Precompute factorials
        for i in range(1, A + 1):
            fact[i] = fact[i - 1] * i

        result = []
        for i in range(A, 0, -1):
            f = fact[i - 1]
            index = B // f
            B %= f
            result.append(str(nums[index]))
            nums.pop(index)

        return ''.join(result)





# CPP


int fact(int n)
{
    if (n>12)   
        return INT_MAX;
    int f = 1;
    for (auto i = 2; i<=n; ++i)
        f *= i;
    return f;
}
string backtracking(int k, vector<int>& numlist)
{
    auto n = numlist.size();
    if (n==0 || k > fact(n))
        return "";
    int f = fact(n-1);
    int pos = k / f;
    k %= f;
    string ch = to_string(numlist[pos]);
    numlist.erase(numlist.begin() + pos);
    return ch + backtracking(k, numlist);
}
string Solution::getPermutation(int n, int k) {
    vector<int> numlist;
    
    for (auto i = 1; i<n+1; ++i)
        numlist.emplace_back(i);
    return backtracking(k-1, numlist);
}

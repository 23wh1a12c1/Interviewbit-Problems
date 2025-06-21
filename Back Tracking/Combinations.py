# Python3

class Solution:
    # @param A : integer (n)
    # @param B : integer (k)
    # @return a list of list of integers
    def combine(self, A, B):
        result = []
        self._backtrack(1, A, B, [], result)
        return result

    # Helper function to perform backtracking
    def _backtrack(self, start, n, k, current, result):
        # If the combination is of size k, add to result
        if k == 0:
            result.append(current[:])  # Add a copy of current
            return

        # Explore all numbers from start to n
        for i in range(start, n + 1):
            current.append(i)  # Choose
            self._backtrack(i + 1, n, k - 1, current, result)  # Explore
            current.pop()  # Unchoose (backtrack)



# JAVA


public class Solution {

    public ArrayList<ArrayList<Integer>> combine(int A, int B) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        ArrayList<Integer> current = new ArrayList<>();
        backtrack(A, B, 1, current, result);
        return result;
    }

    private void backtrack(int n, int k, int start, ArrayList<Integer> current, ArrayList<ArrayList<Integer>> result) {
        if (k == 0) {
            result.add(new ArrayList<>(current));
            return;
        }

        for (int i = start; i <= n; i++) {
            current.add(i);
            backtrack(n, k - 1, i + 1, current, result);
            current.remove(current.size() - 1);
        }
    }
}




# CPP



void comb(int n, int k, int st, vector<vector<int> > &v, vector<int> v1)
{
    if(k == 0)
    {
        v.push_back(v1);
        return;
    }
    for(auto i=st; i<=n; i++)
    {
        v1.push_back(i);
        comb(n, k-1, i+1, v, v1);
        v1.pop_back();
    }
}

vector<vector<int> > Solution::combine(int n, int k) 
{
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    vector<vector<int> > v;
    vector<int> v1;
    
    comb(n, k, 1, v, v1);
    sort(v.begin(), v.end());
    
    return v;
}

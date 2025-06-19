# Java


public class Solution {
    public ArrayList<ArrayList<Integer>> combinationSum(ArrayList<Integer> A, int B) {
        Collections.sort(A); // Sort to handle duplicates and maintain order
        ArrayList<Integer> unique = new ArrayList<>();
        
        // Remove duplicates
        for (int i = 0; i < A.size(); i++) {
            if (i == 0 || !A.get(i).equals(A.get(i - 1))) {
                unique.add(A.get(i));
            }
        }

        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        backtrack(0, unique, B, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int index, ArrayList<Integer> A, int target,
                           ArrayList<Integer> current, ArrayList<ArrayList<Integer>> result) {
        if (target == 0) {
            result.add(new ArrayList<>(current));
            return;
        }

        if (target < 0 || index == A.size()) return;

        // Include A.get(index)
        current.add(A.get(index));
        backtrack(index, A, target - A.get(index), current, result);
        current.remove(current.size() - 1);

        // Exclude A.get(index)
        backtrack(index + 1, A, target, current, result);
    }
}


'''

void backtracking(int start, vector<int>& row, int sum, vector<vector<int> >& res, vector<int>& A, int B)
{
    if (sum >= B)
    {
        if (sum==B)
            res.emplace_back(row);
        return;
    }
    
    if (start == A.size())
        return;
        
    row.emplace_back(A[start]);
    sum += A[start];
    backtracking(start, row, sum, res, A, B);
    sum -= row[row.size()-1];
    row.pop_back();
    backtracking(start+1, row, sum, res, A, B);
}
vector<vector<int> > Solution::combinationSum(vector<int> &A, int B) {
    vector<vector<int> > res;
    vector<int> row, a;
    sort(A.begin(), A.end());
    
    a.emplace_back(A[0]);
    for (auto i = 1; i<A.size(); ++i)
        if (A[i-1] != A[i])
            a.emplace_back(A[i]);
    
    backtracking(0, row, 0, res, a, B);
    return res;
}

'''

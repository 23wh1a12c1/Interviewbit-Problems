# Java


public class Solution {
    public ArrayList<ArrayList<Integer>> combinationSum(ArrayList<Integer> a, int b) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        Collections.sort(a);
        backtrack(0, b, new ArrayList<>(), a, result);
        return result;
    }

    private void backtrack(int start, int target, ArrayList<Integer> temp, ArrayList<Integer> a, ArrayList<ArrayList<Integer>> result) {
        if (target == 0) {
            result.add(new ArrayList<>(temp));
            return;
        }

        for (int i = start; i < a.size(); i++) {
            if (i > start && a.get(i).equals(a.get(i - 1))) continue; // skip duplicates
            if (a.get(i) > target) break; // no need to continue

            temp.add(a.get(i));
            backtrack(i + 1, target - a.get(i), temp, a, result);
            temp.remove(temp.size() - 1);
        }
    }
}



# cpp



void backtracking(int start, vector<int>& row, int sum, vector<vector<int> >& res, vector<int>& A, int B)
{
    if (sum==B)
    {
        /*vector<int> lastRow;              // Simple layman approach to avoid repeated subsets.
        if (!res.empty())                   // Uncomment this block and code will still work.
            lastRow = res[res.size()-1];
        if (res.empty() || lastRow != row)*/
            res.emplace_back(row);
        return;
    }
    
    if (sum > B || start == A.size())
        return;
        
    row.emplace_back(A[start]);
    sum += A[start];
    backtracking(start+1, row, sum, res, A, B);
    sum -= row[row.size()-1];
    row.pop_back();
    
    int endIndex = 0;                       // Refined memory saving way to avoid repeated subsets.
    for (endIndex = start+1; endIndex < A.size() && A[endIndex]==A[start]; ++endIndex)
        ++start;
        
    backtracking(start+1, row, sum, res, A, B); // endIndex = start+1; so passing endIndex will also work.
}

vector<vector<int> > Solution::combinationSum(vector<int> &A, int B) {
    vector<vector<int> > res;
    vector<int> row;
    sort(A.begin(), A.end());
    backtracking(0, row, 0, res, A, B);
    return res;
}


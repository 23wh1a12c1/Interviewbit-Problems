# CPP

void backtracking(int start, vector<vector<int> >& result, vector<int>& A, vector<int>& row)
{
    int size = A.size();
    if (start>=size)
    {
        /*auto s = result.size();   //Valid, but got TLE for this.
        if (s==0)
            result.emplace_back(row);
        else
        {
            while(s>0)
            {
                vector<int> temp = result[s-1];
                --s;
                if (temp == row)
                    return;
            }
            result.emplace_back(row);
        }
        return;*/
        result.emplace_back(row);
        return;
    }
    
    auto currIndex = start + 1;
    while (currIndex<A.size() && A[currIndex]==A[start])
        ++currIndex;
        
    for (auto i = 0; i<=currIndex-start; ++i)
    {
        for (auto j = 0; j<i; ++j)
            row.emplace_back(A[start]);
        backtracking(currIndex, result, A, row);
        for (auto j = 0; j<i; ++j)
            row.pop_back();
    }
}
vector<vector<int> > Solution::subsetsWithDup(vector<int> &A) {
    vector<vector<int> > result;
    vector<int> row;
    sort(A.begin(), A.end());
    backtracking(0, result, A, row);
    sort(result.begin(), result.end());
    return result;
}




# PYTHON3



class Solution:
    def subsetsWithDup(self, A):
        result = []
        A.sort()

        def backtrack(start, path):
            result.append(path[:])  

            for i in range(start, len(A)):
                if i > start and A[i] == A[i - 1]:
                    continue
                path.append(A[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result



# JAVA



import java.util.*;

public class Solution {
    public ArrayList<ArrayList<Integer>> subsetsWithDup(ArrayList<Integer> A) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        Collections.sort(A); 
        backtrack(0, A, new ArrayList<>(), result);
        return result;
    }

    private void backtrack(int start, ArrayList<Integer> A, ArrayList<Integer> path, ArrayList<ArrayList<Integer>> result) {
        result.add(new ArrayList<>(path)); 

        for (int i = start; i < A.size(); i++) {
            if (i > start && A.get(i).equals(A.get(i - 1))) continue;

            path.add(A.get(i));
            backtrack(i + 1, A, path, result);
            path.remove(path.size() - 1); 
        }
    }
}

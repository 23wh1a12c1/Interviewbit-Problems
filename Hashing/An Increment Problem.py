# CPP



vector<int> Solution::solve(vector<int> &A) {
    vector<int> res;
    for(int i=0;i<A.size();i++)
    {
        auto it=find(res.begin(),res.end(),A[i]);
        if(it!=res.end())
        {
            (*it)++;
            res.push_back(A[i]);
        }
        else
        {
            res.push_back(A[i]);
        }
    }
    return res;
}





# JAVA




public class Solution {
    public ArrayList<Integer> solve(ArrayList<Integer> A) {
        ArrayList<Integer> res = new ArrayList<>();
        
        for (int i = 0; i < A.size(); i++) {
            int idx = res.indexOf(A.get(i));
            if (idx != -1) {
                res.set(idx, res.get(idx) + 1); // increment the first occurrence
                res.add(A.get(i)); // add current element again
            } else {
                res.add(A.get(i));
            }
        }
        
        return res;
    }
}







# PYTHON3






class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        res = []
        for val in A:
            if val in res:
                idx = res.index(val)
                res[idx] += 1  # increment first occurrence
                res.append(val)
            else:
                res.append(val)
        return res

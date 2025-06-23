# CPP



void permutation(vector<int> &A, int st, vector<vector<int> > &v)
{
    if(st >= A.size())
    {
        v.push_back(A);
        return;
    }
    for(auto i=st; i<A.size(); i++)
    {
        swap(A[st], A[i]);
        permutation(A, st+1, v);
        swap(A[st], A[i]);
    }
}

vector<vector<int> > Solution::permute(vector<int> &A) 
{
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    vector<vector<int> > v;
    
    permutation(A, 0, v);
    
    return v;
}



# JAVA


import java.util.*;

public class Solution {
    public ArrayList<ArrayList<Integer>> permute(ArrayList<Integer> A) {
        ArrayList<ArrayList<Integer>> result = new ArrayList<>();
        backtrack(0, A, result);
        return result;
    }

    private void backtrack(int start, ArrayList<Integer> A, ArrayList<ArrayList<Integer>> result) {
        if (start == A.size()) {
            result.add(new ArrayList<>(A)); // Make a copy
            return;
        }

        for (int i = start; i < A.size(); i++) {
            Collections.swap(A, start, i);
            backtrack(start + 1, A, result);
            Collections.swap(A, start, i); // Backtrack
        }
    }

    // Example usage
    public static void main(String[] args) {
        Solution sol = new Solution();
        ArrayList<Integer> input = new ArrayList<>(Arrays.asList(1, 2, 3));
        ArrayList<ArrayList<Integer>> permutations = sol.permute(input);

        for (ArrayList<Integer> p : permutations) {
            System.out.println(p);
        }
    }
}




# PYTHON3


def permute(A):
    result = []

    def backtrack(start):
        if start == len(A):
            result.append(A[:])  # Copy the current permutation
            return
        for i in range(start, len(A)):
            A[start], A[i] = A[i], A[start]  # Swap
            backtrack(start + 1)
            A[start], A[i] = A[i], A[start]  # Backtrack

    backtrack(0)
    return result

# Example usage
A = [1, 2, 3]
permutations = permute(A)
for p in permutations:
    print(p)

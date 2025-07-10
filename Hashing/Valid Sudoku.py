# CPP




int Solution::isValidSudoku(const vector<string> &A) 
{
    // Do not write main() function.
    // Do not read input, instead use the arguments to the function.
    // Do not print the output, instead return values as specified
    // Still have a doubt. Checkout www.interviewbit.com/pages/sample_codes/ for more details

    
    int row[9][9] = {0}, col[9][9] = {0}, cube[9][9] = {0};
            
    for(auto i=0; i<A.size(); i++)
    {
        for(auto j=0; j<A.size(); j++)
        {
            if(A[i][j] != '.')
            {
                int ch = A[i][j] - '0' - 1;
                int k = i/3 * 3 + j/3;
            
                if(row[i][ch]++ || col[j][ch]++ || cube[k][ch]++)
                    return false;
            }
            
        }
    }

    return true;
}






#  PYTHON3





class Solution:
    # @param A : tuple of strings
    # @return an integer
    def isValidSudoku(self, A):
        row = [[0]*9 for _ in range(9)]
        col = [[0]*9 for _ in range(9)]
        cube = [[0]*9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                if A[i][j] != '.':
                    ch = int(A[i][j]) - 1
                    k = (i // 3) * 3 + (j // 3)

                    if row[i][ch] or col[j][ch] or cube[k][ch]:
                        return 0  # False (invalid)
                    
                    row[i][ch] = col[j][ch] = cube[k][ch] = 1

        return 1  # True (valid)




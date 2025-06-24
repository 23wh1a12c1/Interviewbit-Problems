# PYTHON

class Solution:
    def solveNQueens(self, A):
        def isSafe(board, row, col):
            # Check left side of the row
            for j in range(col):
                if board[row][j] == 'Q':
                    return False
            
            # Check upper left diagonal
            i, j = row, col
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            
            # Check lower left diagonal
            i, j = row, col
            while i < A and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i += 1
                j -= 1
            
            return True

        def backtrack(col):
            if col == A:
                solution = [''.join(row) for row in board]
                result.append(solution)
                return
            
            for i in range(A):
                if isSafe(board, i, col):
                    board[i][col] = 'Q'
                    backtrack(col + 1)
                    board[i][col] = '.'

        if A == 2 or A == 3:
            return []

        board = [['.' for _ in range(A)] for _ in range(A)]
        result = []
        backtrack(0)
        return result




# JAVA


import java.util.*;

public class Solution {
    public List<List<String>> solveNQueens(int A) {
        List<List<String>> result = new ArrayList<>();
        
        if (A == 2 || A == 3) return result;

        char[][] board = new char[A][A];
        for (int i = 0; i < A; i++) {
            Arrays.fill(board[i], '.');
        }

        backtrack(result, board, 0, A);
        return result;
    }

    private void backtrack(List<List<String>> result, char[][] board, int col, int N) {
        if (col == N) {
            List<String> solution = new ArrayList<>();
            for (char[] row : board) {
                solution.add(new String(row));
            }
            result.add(solution);
            return;
        }

        for (int row = 0; row < N; row++) {
            if (isSafe(board, row, col, N)) {
                board[row][col] = 'Q';
                backtrack(result, board, col + 1, N);
                board[row][col] = '.';
            }
        }
    }

    private boolean isSafe(char[][] board, int row, int col, int N) {
        // Check row on left
        for (int j = 0; j < col; j++) {
            if (board[row][j] == 'Q') return false;
        }

        // Check upper diagonal on left
        for (int i = row, j = col; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 'Q') return false;
        }

        // Check lower diagonal on left
        for (int i = row, j = col; i < N && j >= 0; i++, j--) {
            if (board[i][j] == 'Q') return false;
        }

        return true;
    }
}





# CPP



bool isSafe(vector<vector<string> >& board, int row, int col, int N)
{
    //check left side rows
    for (auto j = 0; j<col; ++j)
        if (board[row][j] == "Q")
            return false;
    
    //check top left side diagonal
    for (auto i = row, j = col; i>-1 && j>-1; --i, --j)
        if (board[i][j] == "Q")
            return false;
            
    //check bottom left side diagonal
    for (auto i = row, j = col; i<N && j>-1; ++i, --j)
        if (board[i][j] == "Q")
            return false;
    
    return true;
}
bool backtracking(vector<vector<string> >& board, int col, vector<vector<string> >& testboard, int N)
{
    if (col == N)
    {
        vector<string> emptyRow;
        board.emplace_back(emptyRow);
        int size = board.size();
        
        for (auto i = 0; i<N; ++i)
        {
            string row = "";
            for (auto j = 0; j<N; ++j)
                row += testboard[i][j];
            
            board[size-1].emplace_back(row);
        }
        return false;
    }
    
    for (auto i = 0; i<N; ++i)
    {
        if (isSafe(testboard, i, col, N))
        {
            testboard[i][col] = "Q";
            
            if (!backtracking(board, col+1, testboard, N))
                testboard[i][col] = ".";
            else
                return true;
        }
    }
    return false;
}
vector<vector<string> > Solution::solveNQueens(int A) {
    vector<vector<string> > testboard;
    
    if (A==2 || A==3)
        return testboard;
    
    vector<string> row(A, ".");
    
    for (auto i = 0; i<A; ++i)
        testboard.emplace_back(row);
    
    vector<vector<string> > board;
    backtracking(board, 0, testboard, A);
    return board;
}












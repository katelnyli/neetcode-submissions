class Solution {
    public boolean isValidSudoku(char[][] board) {
        // track seen nums across rows, cols, squares
        HashSet<Character>[] rows = new HashSet[9];
        HashSet<Character>[] cols = new HashSet[9];
        HashSet<Character>[] squares = new HashSet[9];

        for (int i = 0; i < 9; i++) {
            rows[i] = new HashSet<>();
            cols[i] = new HashSet<>();
            squares[i] = new HashSet<>();
        }

        for (int r = 0; r < 9; r++) {
            for (int c = 0; c < 9; c++) {
                char val = board[r][c];
                if (val == '.') continue;

                int squareIdx = (r / 3) * 3 + (c / 3);

                if (rows[r].contains(val) || 
                    cols[c].contains(val) || 
                    squares[squareIdx].contains(val)) {
                        return false;
                } 

                rows[r].add(val);
                cols[c].add(val);
                squares[squareIdx].add(val);

            }
        }
        return true;
    }
}

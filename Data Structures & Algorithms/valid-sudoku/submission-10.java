class Solution {
    public boolean isValidSudoku(char[][] board) {
        return checkRows(board) && checkColumns(board) && checkBoxes(board);
    }

    public boolean checkRows(char[][] board) {
        List<Integer> nums = new ArrayList<>();
        for (int i = 0; i < board.length; i++) {
            for (int j = 0; j < board[i].length; j++) {
                if (board[i][j] == '.') continue;
                if (nums.contains(board[i][j] - '0')) return false;
                else nums.add(board[i][j] - '0');
            }
            nums.clear();
        }
        return true;
    }

    public boolean checkColumns(char[][] board) {
        List<Integer> nums = new ArrayList<>();
        for (int i = 0; i < board[0].length; i++) {
            for (int j = 0; j < board.length; j++) {
                if (board[j][i] == '.') continue;
                if (nums.contains(board[j][i] - '0')) return false;
                else nums.add(board[j][i] - '0');
            }
            nums.clear();
        }
        return true;
    }

    public boolean checkBoxes(char[][] board) {
        List<Integer> nums = new ArrayList<>();
        for (int i = 0; i < board.length; i+=3) {
            for (int j = 0; j < board[0].length; j+=3) {
                for (int k = 0; k < 3; k++) {
                    for (int l = 0; l < 3; l++) {
                        if (board[i + k][j + l] == '.') continue;
                        if (nums.contains(board[i + k][j + l] - '0')) return false;
                        else nums.add(board[i + k][j + l] - '0');
                    }
                }
                nums.clear();
            }
        }
        return true;
    }
}

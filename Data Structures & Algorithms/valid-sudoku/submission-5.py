def checkRows(board):
    validRows = True
    for x in board:
        digits = [0]*10
        for y in x:
            if y != ".":
                if digits[int(y)] != 0:
                    validRows = False
                else:
                    digits[int(y)] = y
    return validRows
    
def checkColumns(board):
    validColumns = True
    for x in range(9):
        digits = [0]*10
        for y in range(9):
            if board[y][x] != ".":
                if digits[int(board[y][x])] != 0:
                    validColumns = False
                else:
                    digits[int(board[y][x])] = board[y][x]
    return validColumns

def checkBoxes(board):
    validBoxes = True
    for i in range(3):
        for j in range(3):
            nums =( [board[i*3][j*3], board[i*3][j*3+1], board[i*3][j*3+2],
                    board[i*3+1][j*3], board[i*3+1][j*3+1], board[i*3+1][j*3+2],
                    board[i*3+2][j*3], board[i*3+2][j*3+1], board[i*3+2][j*3+2]]
            )
            digits = [0]*10
            for x in range(9):
                if nums[x] != ".":
                    if digits[int(nums[x])] != 0:
                        validBoxes = False
                    else:
                        digits[int(nums[x])] = int(nums[x])
    return validBoxes

class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return checkRows(board) and checkColumns(board) and checkBoxes(board)

    


    
def check_horizontal(board, rows, cols):
    for row in range(rows):
        for col in range(cols - 3):
            if board[row][col] != 0 and board[row][col] == board[row][col+1] == board[row][col+2] == board[row][col+3]:
                return {(row, col), (row, col+3)}

def check_vertical(board, rows, cols):
    for row in range(rows - 3):
        for col in range(cols):
            if board[row][col] != 0 and board[row][col] == board[row+1][col] == board[row+2][col] == board[row+3][col]:
                return {(row, col), (row+3, col)}
            
def check_diagonal(board, rows, cols):
    # Check diagonal (top-left to bottom-right)
    for row in range(rows - 3):
        for col in range(cols - 3):
            if board[row][col] != 0 and board[row][col] == board[row+1][col+1] == board[row+2][col+2] == board[row+3][col+3]:
                return {(row, col), (row+3, col+3)}
    # Check diagonal (top-right to bottom-left)
    for row in range(rows - 3):
        for col in range(3, cols):
            if board[row][col] != 0 and board[row][col] == board[row+1][col-1] == board[row+2][col-2] == board[row+3][col-3]:
                return {(row, col), (row+3, col-3)}
            
def four_in_line(board):
    rows = len(board)
    cols = len(board[0])

    result = check_horizontal(board, rows, cols)
    if result is None:
        result = check_vertical(board, rows, cols)
    if result is None:
        result = check_diagonal(board, rows, cols)

    return result

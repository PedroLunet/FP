def tic_tac_toe(board, player):
    lines = board.split("\n")
    board_size = len(lines)
   
    row_letter = 64
    for line in lines:
        row_letter += 1
        count = line.count(player)
        try:
            if count == (board_size - 1):
                return (chr(row_letter) + str(line.index(" ") + 1))
        except:
            pass

    col_letter = 65
    columns = []
    for i in range(board_size):
        column = ""
        for j in range(board_size):
            column += lines[j][i]
        columns.append(column)
    for column in columns:
        count = column.count(player)
        try:
            if count == (board_size - 1):
                return (chr(col_letter + column.index(" ")) + str(columns.index(column) + 1))
        except:
            pass

    diagonal1 = ""
    diagonal2 = ""
    for m in range(board_size):
        diagonal1 += lines[m][m]
        diagonal2 += lines[m][board_size - 1 - m]
    diagonals = [diagonal1, diagonal2]
    for diagonal in diagonals:
        count = diagonal.count(player)
        try:
            if count == (board_size - 1):
                if diagonals.index(diagonal) == 0:
                    return (chr(col_letter + diagonal.index(" ")) + str(diagonal.index(" ") + 1))
                else:
                    return (chr(col_letter + diagonal.index(" ")) + str((board_size - 1 - diagonal.index(" ")) + 1))
        except:
            pass





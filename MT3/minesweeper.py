def count_mines(board):
    result = []
    for i in range(len(board)):
        auxstr = ""
        for j in range(len(board[i])):
            count = 0

            #1ST LINE SPECIAL CASE
            if i == 0:
                #LEFT CORNER SPECIAL CASE
                if j == 0:
                    if board[i][j + 1] == "*":
                        count += 1
                    if board[i + 1][j] == "*":
                        count += 1
                    if board[i + 1][j + 1] == "*":
                        count += 1
                #RIGHT CORNER SPECIAL CASE
                elif j == len(board[i]) - 1:
                    if board[i][j - 1] == "*":
                        count += 1
                    if board[i + 1][j] == "*":
                        count += 1
                    if board[i + 1][j - 1] == "*":
                        count += 1
                #REST OF THE 1ST LINE SPECIAL CASE
                else:
                    if board[i][j + 1] == "*":
                        count += 1
                    if board[i][j - 1] == "*":
                        count += 1
                    if board[i + 1][j] == "*":
                        count += 1
                    if board[i + 1][j + 1] == "*":
                        count += 1
                    if board[i + 1][j - 1] == "*":
                        count += 1
                auxstr += str(count)

            #LAST LINE SPECIAL CASE
            elif i == len(board) - 1:
                #LEFT CORNER SPECIAL CASE
                if j == 0:
                    if board[i][j + 1] == "*":
                        count += 1
                    if board[i - 1][j] == "*":
                        count += 1
                    if board[i - 1][j + 1] == "*":
                        count += 1
                #RIGHT CORNER SPECIAL CASE
                elif j == len(board[i]) - 1:
                    if board[i][j - 1] == "*":
                        count += 1
                    if board[i - 1][j] == "*":
                        count += 1
                    if board[i - 1][j - 1] == "*":
                        count += 1
                #REST OF THE LAST LINE SPECIAL CASE
                else:
                    if board[i][j + 1] == "*":
                        count += 1
                    if board[i][j - 1] == "*":
                        count += 1
                    if board[i - 1][j] == "*":
                        count += 1
                    if board[i - 1][j + 1] == "*":
                        count += 1
                    if board[i - 1][j - 1] == "*":
                        count += 1
                auxstr += str(count)
        
            else:
                if j == 0:
                    if board[i][j + 1] == "*":
                        count += 1
                    if board[i - 1][j] == "*":
                        count += 1
                    if board[i - 1][j + 1] == "*":
                        count += 1
                    if board[i + 1][j] == "*":
                        count += 1
                    if board[i + 1][j + 1] == "*":
                        count += 1
                elif j == len(board[i]) - 1:
                    if board[i][j - 1] == "*":
                        count += 1
                    if board[i - 1][j] == "*":
                        count += 1
                    if board[i - 1][j - 1] == "*":
                        count += 1
                    if board[i + 1][j] == "*":
                        count += 1
                    if board[i + 1][j - 1] == "*":
                        count += 1
                else:
                    if board[i][j + 1] == "*":
                        count += 1
                    if board[i][j - 1] == "*":
                        count += 1
                    if board[i - 1][j] == "*":
                        count += 1
                    if board[i - 1][j + 1] == "*":
                        count += 1
                    if board[i - 1][j - 1] == "*":
                        count += 1
                    if board[i + 1][j] == "*":
                        count += 1
                    if board[i + 1][j + 1] == "*":
                        count += 1
                    if board[i + 1][j - 1] == "*":
                        count += 1
                auxstr += str(count)
        result.append(auxstr)
    return result

                                        
                
                    





print(count_mines(['......', '.**.*.', '......']))
#['122211', '111201', '122211']

print(count_mines(['.....', '*.*.*', '.*.*.', '..*..']))
#['12121', '13231', '23432', '12221']

print(count_mines(['.***.', '.**..', '..*..', '*...*', '*.*.*']))
#['23421', '24541', '24231', '14241', '13031']

print(count_mines(['..***.**..', '****.*****', '****.*.***', '.*.******.', '*...*..***', '*.********', '********..', '.*.*******', '*.***.****', '****..****']))
#['2444344442', '3676646663', '4675758774', '4454545675', '2446677774', '3646666663', '3567888774', '4577777763', '3666566885', '2444333553']
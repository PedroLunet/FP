def magic(mat):
    n = len(mat)
    target_sum = sum(mat[0])
    
    for row in mat:
        if sum(row) != target_sum:
            return False
    
    for j in range(n):
        col_sum = 0
        for i in range(n):
            col_sum += mat[i][j]
        if col_sum != target_sum:
            return False
    
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += mat[i][i]
    if diagonal_sum != target_sum:
        return False
    
    diagonal_sum = 0
    for i in range(n):
        diagonal_sum += mat[i][n-i-1]
    if diagonal_sum != target_sum:
        return False
    
    return True


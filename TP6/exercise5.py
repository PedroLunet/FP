
def mult(M, N):

    m_rows, m_cols = len(M), len(M[0])
    n_rows, n_cols = len(N), len(N[0])
        

    if m_cols != n_rows:
        return []
        
  
    result = [[0 for _ in range(n_cols)] for _ in range(m_rows)]
        

    for i in range(m_rows):
        for j in range(n_cols):
            for k in range(m_cols):
                result[i][j] += M[i][k] * N[k][j]
        
    return result

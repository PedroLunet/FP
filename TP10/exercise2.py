import math

def comprehensions(i, j):
    numbers_3_8 = [num for num in range(i, j+1) if str(num)[-1] in ['3', '8']]
    
    square_roots = tuple(round(math.sqrt(num), 2) for num in range(i, j+1))
    
    ascii_dict = {num: chr(num) for num in range(i, j+1)}
    
    return (numbers_3_8, square_roots, ascii_dict)

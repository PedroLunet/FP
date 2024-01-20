import math

def comprehensions(i, j):
    int3_8 = [x for x in range(i, j + 1) if str(x)[-1] == "3" or str(x)[-1] == "8"]
    tup = tuple(round(math.sqrt(x), 2) for x in range(i, j + 1))
    dicval = {x:chr(x) for x in range(i, j + 1)}
    return (int3_8, tup, dicval)

print(comprehensions(0, 0))
#([], (0.0,), {0: '\x00'})

print(comprehensions(100, 102))
#([], (10.0, 10.05, 10.1), {100: 'd', 101: 'e', 102: 'f'})

print(comprehensions(110, 115))
#([113], (10.49, 10.54, 10.58, 10.63, 10.68, 10.72), {110: 'n', 111: 'o', 112: 'p', 113: 'q', 114: 'r', 115: 's'})

print(comprehensions(63, 69))
#([63, 68], (7.94, 8.0, 8.06, 8.12, 8.19, 8.25, 8.31), {63: '?', 64: '@', 65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E'})

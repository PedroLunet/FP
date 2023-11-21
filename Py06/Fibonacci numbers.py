def fib(n):
    fibl = [0, 1]
    if n <= 2:
        return fibl[:n]
    else:
        for i in range(2, n):
            fibl.append(fibl[i - 1] + fibl[i - 2])
        return fibl

def evaluate(a, x):
    func = lambda i: a[i] * (x ** i)
    return sum(map(func, range(len(a))))


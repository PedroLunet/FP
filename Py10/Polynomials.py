def evaluate(a, x):
    lst = [a[i] * x ** i for i in range(len(a))]
    return sum(lst)


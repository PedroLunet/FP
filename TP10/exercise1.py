def square_odds(values):
    alist = list(values.split(","))
    result = [int(x)**2 for x in alist if int(x) % 2 != 0]
    return result
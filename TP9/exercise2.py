
def variance(alist):
    n = len(alist)
    mean = sum(alist) / n
    squared_diff = map(lambda x: (x - mean) ** 2, alist)
    return round(sum(squared_diff) / n, 3)

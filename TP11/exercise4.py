
def bisect(f, n):
    lower = 0
    upper = 1

    for _ in range(n):
        midpoint = (lower + upper) / 2
        if f(lower) * f(midpoint) > 0:
            lower = midpoint
        else:
            upper = midpoint

    return round(midpoint, 5)

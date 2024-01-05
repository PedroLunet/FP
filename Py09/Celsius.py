def to_celsius(t):
    x = lambda temp: round((temp - 32) * 5/9, 1)
    return list(map(x, t))
    
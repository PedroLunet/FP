def to_fahrenheit(t):
    x = lambda temp: round((temp * 9/5) + 32, 2)
    return list(map(x, t))
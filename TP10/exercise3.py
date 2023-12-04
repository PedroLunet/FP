def pythagoreans(a: int, b: int):
    r = range(a, b)
    values = [(x, y, z) for x in r for y in range(x, b) for z in r if x**2 + y**2 == z**2]
    return values   

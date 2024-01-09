def pythagoreans(a, b):
    return [tuple(sorted((x, y, z))) for x in range(a, b) for y in range(x, b) for z in range(a, b) if (x**2 + y**2) == z**2]


print(pythagoreans(1, 10))
#[(3, 4, 5)]

print(pythagoreans(10, 20))
#[]

print(pythagoreans(10, 30))
#[(10, 24, 26), (12, 16, 20), (15, 20, 25), (20, 21, 29)]

print(pythagoreans(51, 91))
#[(51, 68, 85), (54, 72, 90), (60, 63, 87)] 

def triplet(tup):
    for x in range(len(tup)):
        for y in range(x + 1, len(tup)):
            for z in range(y + 1, len(tup)):
                if tup[x] + tup[y] + tup[z] == 0:
                    a = tup[x]
                    b = tup[y]
                    c = tup[z]
                    return (a, b, c)
    return ()


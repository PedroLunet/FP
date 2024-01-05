def rearrange(l):
    neg = [x for x in l if x <= 0]
    print(neg)
    pos = [x for x in l if x > 0]
    print(pos)
    return neg + pos

print(rearrange([12, 11, -13, -5, 6, -7, 5, -3, -6, 0]))
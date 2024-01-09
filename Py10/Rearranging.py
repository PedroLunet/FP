def rearrange(l):
    neg = [x for x in l if x <= 0]
    pos = [x for x in l if x > 0]
    return neg + pos

def gcd_rec(a, b):
    div = 1
    if a == 0 or b == 0:
        return 0
    elif a % b == 0:
        return b
    else:
        div = gcd_rec(b, a % b)
    return div

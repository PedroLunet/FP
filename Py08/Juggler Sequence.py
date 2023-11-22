import math

def juggler(n, p):
    if p == 0:
        return n
    if juggler(n, p-1) % 2 == 0:
        return int(math.sqrt(juggler(n, p - 1)))
    else:
        return int((juggler(n, p - 1))**(3/2))
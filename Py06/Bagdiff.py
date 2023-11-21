def bagdiff(xs, ys):
    result = xs.copy()
    for y in ys:
        if y in result:
            result.remove(y)
    return result
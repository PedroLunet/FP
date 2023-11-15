def local_minima(alist):
    result = []
    for i in range(1, len(alist)-1):
        window = alist[i-1:i+2]
        if window.count(min(window)) == 1:
            result.append(min(window))
    return result

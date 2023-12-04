def merge(xs, ys):
    result = []
    i = j = 0
    while i < len(xs) and j < len(ys):
        if xs[i] < ys[j]:
            result.append(xs[i])
            i += 1
        else:
            result.append(ys[j])
            j += 1

    # Add the remaining elements from both lists, if any
    result.extend(xs[i:])
    result.extend(ys[j:])

    return result

def msort(xs):
    if len(xs) <= 1:
        return xs
    
    mid = len(xs) // 2
    left_half = xs[:mid]
    right_half = xs[mid:]
    
    sorted_left = msort(left_half)
    sorted_right = msort(right_half)
    
    return merge(sorted_left, sorted_right)

def find_me(f, limits):
    left, right = limits
    count = 0

    while left <= right:
        mid = (left + right) // 2
        result = f(mid)
        count += 1

        if result == 0:
            return count
        elif result == -1:
            right = mid - 1
        else:
            left = mid + 1

    return -1  

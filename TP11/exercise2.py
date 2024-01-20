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


print(find_me(lambda n: -1 if n > 30 else 1 if n < 30 else 0, (0, 100)))	

#4

print(find_me(lambda n: -1 if n > 563 else 1 if n < 563 else 0, (-5000, 5000)))

#13

print(find_me(lambda n: -1 if n > -891 else 1 if n < -891 else 0, (-1000, 10000)))

#14

print(find_me(lambda n: 0 if n == 99 else 1, (0, 100)))

#6
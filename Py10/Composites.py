def get_composites(n):
    for num in range(4, n+1):
        for i in range(2, num):
            if num % i == 0:
                yield num
                break


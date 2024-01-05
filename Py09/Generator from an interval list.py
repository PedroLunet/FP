def generator(intlist):
    for interval in intlist:
        for num in range(interval[0], interval[1]+1):
            yield num


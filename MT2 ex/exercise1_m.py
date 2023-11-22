def time_diff(time1, time2):
    if time2[0] < time1[0]:
        hrs = time1[0] - time2[0]
        min = 60 - abs(time1[1] - time2[1])
        if time2[1] > time1[1] and time1[0] != time2[0]:
            hrs -= 1
    else:
        hrs = time2[0] - time1[0]
        min = abs(time1[1] - time2[1])
        if time1[1] > time2[1] and time1[0] != time2[0]:
            hrs -= 1
    return (hrs, min)


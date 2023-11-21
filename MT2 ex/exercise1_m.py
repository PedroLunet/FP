def time_diff(time1, time2):
    hrs = abs(time1[0] - time2[0])
    min = abs(time1[1] - time2[1])
    return (hrs, min)

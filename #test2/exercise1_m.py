def time_diff(time1, time2):

    #time in minutes
    t1 = time1[0] * 60 + time1[1]
    t2 = time2[0] * 60 + time2[1]

    #diference in min
    if t2 < t1:
        ft = t1 - t2
    else:
        ft = t2 - t1
    
    #back in hrs.min format
    hrs = ft // 60
    minutes = ft - hrs * 60

    return (hrs, minutes)


#Hidden Tests

print(time_diff((0, 0), (2, 33)))

print(time_diff((2, 33), (0, 1)))

print(time_diff((18, 25), (22, 15)))

print(time_diff((23, 3), (21, 58)))



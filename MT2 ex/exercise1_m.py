def time_diff(time1, time2):
    tt1 = (time1[0] * 60) + time1[1]
    tt2 = (time2[0] * 60) + time2[1]
    h = 0
    m = 0
    
    if tt2 < tt1:
        auxr = tt1 - tt2
    else:
        auxr = tt2 - tt1
    
    while auxr >= 60:
        h += 1
        auxr -= 60
    m = auxr

    return (h, m)
        

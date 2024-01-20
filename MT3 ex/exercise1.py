def days_until_christmas(date):
    days_of_month = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
    }
    result = 0
    dd, mm, yy = date
    dc, mc = 25, 12  # Christmas day

    while not (dd == dc and mm == mc):
        result += 1
        dd += 1

        if dd > days_of_month[mm]:
            dd = 1
            mm += 1
            if mm > 12:
                mm = 1
                yy += 1

    return result

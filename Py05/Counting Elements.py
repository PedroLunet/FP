def count_until(tup):
    cnt = 0
    flag = False
    for i in tup:
        if type(i) == type(tup):
            flag = True
            break
        else:
            cnt += 1
    if flag == False:
        return -1
    else:
        return cnt
def shopping(alist, stock):
    spent = 0
    missing = {}
    for i in alist:
        flag = 0
        for j in stock:
            if i == j:
                if alist[i] <= stock[j][0]: #They have more than you want
                    spent += alist[i] * stock[j][1]
                    flag = 1
                else: #You want more then they have
                    spent += stock[j][0] * stock[j][1]
                    alist[i] -= stock[j][0]
        if flag == 0: #They dont have what you want
            missing[i] = alist[i]
    return (spent, missing)
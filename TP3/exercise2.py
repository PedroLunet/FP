h = int(input())
min = int(input())
flag = 0

if h >= 24 or h < 0 or min >= 60 or min < 0:
    print("INVALID DATE FORMAT")
    exit()
else:
    if h >= 12:
        h -= 12
        flag = 1
    if h == 0:
        h += 12
if flag == 0:
    if min != 0:
        print(str(h) + ":" + str(min).zfill(2) + " am")   
    else:
        print(str(h) + " am")
else:
    if min != 0:
        print(str(h) + ":" + str(min).zfill(2) + " pm")   
    else:
        print(str(h) + " pm")
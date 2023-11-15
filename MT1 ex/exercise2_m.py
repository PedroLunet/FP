PE1 = int(input())
PE2 = int(input())
PE3 = int(input())
PE4 = int(input())


if PE3 < 40:
    if PE4 < 40:
        print("RFF")
    else:
        maxv = max(PE1, PE2, max(PE3, PE4))
        minv = min(PE1, PE2, max(PE3, PE4))
        mid = PE1 + PE2 + max(PE3, PE4) - maxv - minv
        print(int((maxv + mid) / 2))
else:
    maxv = max(PE1, PE2, PE3)
    minv = min(PE1, PE2, PE3)
    mid = PE1 + PE2 + PE3 - maxv - minv
    print(int((maxv + mid) / 2))
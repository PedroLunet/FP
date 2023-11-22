def most_frequent(alist):
    dic = {}
    for i in alist:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    return max(dic, key=lambda k: (dic[k], k), default=None)

def academy_awards(alist):
    result = {}
    for tup in alist:
        movie = tup[1]
        if movie in result:
            result[movie] += 1
        else:
            result[movie] = 1
    return result
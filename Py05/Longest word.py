def longest(s):
    aux_l = s.split()
    max_len = 0
    for i in aux_l:
        if len(i) > max_len:
            max_len = len(i)
    return max_len

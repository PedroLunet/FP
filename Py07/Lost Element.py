def lost_element(s1, s2):
    for i in s1:
        if i not in s2:
            return i
    for j in s2:
        if j not in s1:
            return j

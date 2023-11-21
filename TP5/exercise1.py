def rm_letter_rev(ch, s):
    aux = ""
    for i in s:
        if i != ch:
            aux += i
    return aux[::-1]


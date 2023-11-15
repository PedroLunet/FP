def rm_letter_rev(ch, s):
    new_str = ""
    for i in range(len(s)-1, -1, -1):
        if s[i] != ch:
            new_str += s[i]
    return new_str


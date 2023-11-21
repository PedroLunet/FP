def count_chars(a_string):
    calpha = 0
    cdigit = 0
    cspecial = 0

    for ch in a_string:
        if ch.isalpha():
            calpha += 1
        if ch in "0123456789":
            cdigit += 1
        if ch in '""!@#$%^&*()-+?_=,<>/""':
            cspecial += 1
    return (calpha, cdigit, cspecial)
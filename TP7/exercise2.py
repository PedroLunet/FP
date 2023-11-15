def roman_to_integer(astring):
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    for i in range(len(astring)):
        if i > 0 and romans[astring[i]] > romans[astring[i-1]]:
            result += romans[astring[i]] - 2 * romans[astring[i-1]]
        else:
            result += romans[astring[i]]
    return result

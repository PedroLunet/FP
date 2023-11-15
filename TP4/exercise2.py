    def adigits(a, b, c):
    aux = [a, b, c]
    aux.sort()
    result = ""
    i = 0
    while i < len(aux):
        result += str(aux[i])
        i += 1
    return result


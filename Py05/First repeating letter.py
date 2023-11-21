def repeated_letter(s):
    aux = tuple(s)
    n = len(aux)
    for i in range(n):
        for j in range(i + 1, n):
            if aux[i] == aux[j]:
                return aux[i]
    return None


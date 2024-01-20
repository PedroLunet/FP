def lfsr(n):
    result = "" + n[-1]
    l = len(n)
    xor = 0
    flag = True
    aux = n
    orig = n
    while flag:
        if aux[-1] == aux[-2]:
            xor = 0
        else:
            xor = 1
        n = str(xor) + n
        aux = n[:l]
        if aux != orig:
            result += aux[-1]
        else:
            flag = False
    return result   

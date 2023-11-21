def fetch_middle(llists):
    aux = []
    for i in range(len(llists)):
        if len(llists[i]) % 2 == 0:
            aux.append((llists[i][len(llists[i]) // 2] + llists[i][len(llists[i]) // 2 - 1]) / 2)
        else:
            aux.append(llists[i][len(llists[i]) // 2])
    return aux
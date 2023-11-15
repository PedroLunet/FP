def mask_data(data, n_characters, position):
    if n_characters == 0:
        return data
    elif n_characters < 0 or n_characters > len(data):
        return '*' * len(data)
    elif position == 'begin':
        return '*' * n_characters + data[n_characters:]
    elif position == 'end':
        return data[:-n_characters] + '*' * n_characters


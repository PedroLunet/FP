def switch_dict(adict):
    new_dict = {}
    for key, value in adict.items():
        if value not in new_dict:
            new_dict[value] = [key]
        else:
            new_dict[value].append(key)
    return new_dict


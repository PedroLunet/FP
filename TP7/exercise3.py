def sparse_dot_product(dict1, dict2):
    dot_product = 0

    for key in dict1:
        if key in dict2:
            dot_product += dict1[key] * dict2[key]
    return dot_product

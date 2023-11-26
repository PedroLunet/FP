
def x_union(list1, list2):
    first_components1 = list(map(lambda x: x[0], list1))
    first_components2 = list(map(lambda x: x[0], list2))
    exclusive_components = list(filter(lambda x: (x not in first_components1) or (x not in first_components2), first_components1 + first_components2))
    return list(filter(lambda x: x[0] in exclusive_components, list1 + list2))

def max_path(tree):
    if isinstance(tree, int):
        return tree
    left, value, right = tree
    return value + max(max_path(left), max_path(right))


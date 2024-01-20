def list_paths(dirtree):
    result = []
    root = dirtree[0]
    run = dirtree[1:]
    for i in run:
        if isinstance(i, str):
            result.append(f"{root}/{i}")
        else:
            result.extend(list_paths(i))
    return result
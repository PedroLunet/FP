def search_tree(key, tree):
    visited = []
    while tree is not None:
        node_key, value, left, right = tree
        visited.append(node_key)
        if key == node_key:
            return (value, visited)
        elif key < node_key:
            tree = left
        else:
            tree = right
    return None

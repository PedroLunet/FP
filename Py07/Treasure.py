def treasure(clues):
    visited = set()
    current_location = (0, 0)

    while current_location in clues:
        visited.add(current_location)
        current_location = clues[current_location]

        if current_location in visited:
            break

    return current_location
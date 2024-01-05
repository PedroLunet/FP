def do_not_intersect(rect1, rect2):
    # Check if rect1 is to the left of rect2
    if rect1['x2'] < rect2['x1'] or rect2['x2'] < rect1['x1']:
        return True
    # Check if rect1 is above rect2
    if rect1['y2'] < rect2['y1'] or rect2['y2'] < rect1['y1']:
        return True
    return False

def number_of_collisions(objects):
    collisions = 0
    n = len(objects)

    for i in range(n):
        for j in range(i + 1, n):
            if not do_not_intersect(objects[i], objects[j]):
                collisions += 1

    return collisions



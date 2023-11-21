def map(pos, steps):
    aux_l = steps.split("-")
    x = pos[0]
    y = pos[1]
    for com in aux_l:
        if com == "up":
            y += 1
        if com == "down":
            y -= 1
        if com == "right":
            x += 1
        if com == "left":
            x -= 1
    return (x, y)
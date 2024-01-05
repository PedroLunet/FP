def move_ball(board):
    if not board or not board[0]:
        raise ValueError("Invalid board dimensions")

    valid_directions = {"N", "S", "W", "E"}
    direction_changes = {("S", "/"): "W", ("W", "/"): "S", ("N", "/"): "E", ("E", "/"): "N",
                        ("S", "\\"): "E", ("E", "\\"): "S", ("N", "\\"): "W", ("W", "\\"): "N"}

    current_board = [list(row) for row in board]
    ball_direction = ""
    ball_positions = []
    current_position = ()

    for y in range(len(current_board)):
        for x in range(len(current_board[0])):
            if current_board[y][x] in valid_directions:
                ball_direction = current_board[y][x]
                ball_positions.append((y, x))
                current_position = (y, x)

    while True:
        if ball_direction == "N":
            current_position = (current_position[0] - 1, current_position[1])
        elif ball_direction == "S":
            current_position = (current_position[0] + 1, current_position[1])
        elif ball_direction == "E":
            current_position = (current_position[0], current_position[1] + 1)
        elif ball_direction == "W":
            current_position = (current_position[0], current_position[1] - 1)

        ball_positions.append(current_position)
        if current_board[current_position[0]][current_position[1]] == "X":
            break
        elif current_board[current_position[0]][current_position[1]] in {"/", "\\"}:
            ball_direction = direction_changes.get((ball_direction, current_board[current_position[0]][current_position[1]]), ball_direction)

    return ball_positions

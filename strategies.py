
def convert_coords_to_direction(current_head, x, y):

    if x - current_head["x"] > 0:
        result = "right"
    elif x - current_head["x"] < 0:
        result = "down" # TODO: check logic
    else:
        if y - current_head["y"] > 0:
            result = "up"
        else:
            result = "down"
    
    return result

def convert_direction_to_coords(current_head, next_move):

    future_head = current_head
    print(f"before move: {future_head}")
    if next_move == "right":
        future_head["x"] = current_head["x"] + 1
    elif next_move == "left":
        future_head["x"] = current_head["x"] - 1
    elif next_move == "up":
        future_head["y"] = current_head["y"] + 1
    elif next_move == "down":
        future_head["y"] = current_head["y"] - 1

    return future_head


def avoid_walls(head, move):
    ''' Return true if the move coords will avoid hitting
        a wall, false if it will cause the snake to hit the wall
    '''
    future_head = convert_direction_to_coords(head, move)
    print(future_head)
    if future_head["x"] < 0 or future_head["y"] < 0:
        result = False
    elif future_head["x"] > global_variables.BOARD_MAXIMUM_X or future_head["y"] > global_variables.BOARD_MAXIMUM_Y:
        result = False
    else:
        result = True
    
    return result
    
import global_variables
import strategies

data = {
    "game": {
        "id": "game-00fe20da-94ad-11ea-bb37",
        "ruleset": {
            "name": "standard",
            "version": "v.1.2.3"
        },
        "timeout": 500
    },
    "turn": 14,
    "board": {
        "height": 11,
        "width": 11,
        "food": [
            {"x": 5, "y": 5},
            {"x": 9, "y": 0},
            {"x": 2, "y": 6}
        ],
        "hazards": [
            {"x": 3, "y": 2}
        ],
        "snakes": [
            {
                "id": "snake-508e96ac-94ad-11ea-bb37",
                "name": "My Snake",
                "health": 54,
                "body": [
                        {"x": 0, "y": 0},
                        {"x": 1, "y": 0},
                        {"x": 2, "y": 0}
                ],
                "latency": "111",
                "head": {"x": 0, "y": 0},
                "length": 3,
                "shout": "why are we shouting??",
                "squad": ""
            },
                        {
                "id": "snake-508e96ac-94ad-1639-be12",
                "name": "Snaaaaake",
                "health": 54,
                "body": [
                        {"x": 2, "y": 3},
                        {"x": 2, "y": 2},
                        {"x": 2, "y": 1},
                        {"x": 1, "y": 1},
                        {"x": 0, "y": 1}
                ],
                "latency": "111",
                "head": {"x": 2, "y": 3},
                "length": 5,
                "shout": "why are we shouting??",
                "squad": ""
            },
            {
                "id": "snake-b67f4906-94ae-11ea-bb37",
                "name": "Another Snake",
                "health": 16,
                "body": [
                        {"x": 5, "y": 4},
                        {"x": 5, "y": 3},
                        {"x": 6, "y": 3},
                        {"x": 6, "y": 2}
                ],
                "latency": "222",
                "head": {"x": 5, "y": 4},
                "length": 4,
                "shout": "I'm not really sure...",
                "squad": ""
            }
        ]
    },
    "you": {
        "id": "snake-508e96ac-94ad-11ea-bb37",
        "name": "My Snake",
        "health": 54,
        "body": [
                {"x": 0, "y": 0},
                {"x": 1, "y": 0},
                {"x": 2, "y": 0}
        ],
        "latency": "111",
        "head": {"x": 0, "y": 0},
        "length": 3,
        "shout": "why are we shouting??",
        "squad": ""
    }
}

global_variables.BOARD_MAXIMUM_X = data["board"]["width"]
global_variables.BOARD_MAXIMUM_Y = data["board"]["height"]


def test_avoid_walls_direction_up():

    current_head = data["you"]["head"]
    next_move = "up"
    move_coords = strategies.convert_direction_to_coords(
        current_head, next_move)
    isWallAvoided = strategies.avoid_walls(move_coords)
    assert isWallAvoided == True


def test_avoid_walls_direction_down():

    current_head = data["you"]["head"]
    next_move = "down"
    move_coords = strategies.convert_direction_to_coords(
        current_head, next_move)
    isWallAvoided = strategies.avoid_walls(move_coords)
    assert isWallAvoided == False


def test_avoid_walls_direction_left():

    current_head = data["you"]["head"]
    next_move = "left"
    move_coords = strategies.convert_direction_to_coords(
        current_head, next_move)
    isWallAvoided = strategies.avoid_walls(move_coords)
    assert isWallAvoided == False


def test_avoid_walls_direction_right():

    current_head = data["you"]["head"]
    next_move = "right"
    move_coords = strategies.convert_direction_to_coords(
        current_head, next_move)
    isWallAvoided = strategies.avoid_walls(move_coords)
    assert isWallAvoided == True


def test_avoid_self_move_right():
    current_head = data["you"]["head"]
    current_body = data["you"]["body"]
    next_move = "right"
    move_coords = strategies.convert_direction_to_coords(
        current_head, next_move)
    isSelfAvoided = strategies.avoid_self(move_coords, current_body)
    assert isSelfAvoided == False


def test_avoid_self_move_left():
    current_head = data["you"]["head"]
    current_body = data["you"]["body"]
    next_move = "left"
    move_coords = strategies.convert_direction_to_coords(
        current_head, next_move)
    isSelfAvoided = strategies.avoid_self(move_coords, current_body)
    assert isSelfAvoided == True


def test_avoid_self_move_up():
    current_head = data["you"]["head"]
    current_body = data["you"]["body"]
    next_move = "up"
    move_coords = strategies.convert_direction_to_coords(
        current_head, next_move)
    isSelfAvoided = strategies.avoid_self(move_coords, current_body)
    assert isSelfAvoided == True


def test_avoid_self_move_down():
    current_head = data["you"]["head"]
    current_body = data["you"]["body"]
    next_move = "down"
    move_coords = strategies.convert_direction_to_coords(
        current_head, next_move)
    isSelfAvoided = strategies.avoid_self(move_coords, current_body)
    assert isSelfAvoided == True

def test_avoid_snakes():
    current_head = data["you"]["head"]
    all_snakes = []
    current_snakes = data["board"]["snakes"]
    for snake in current_snakes:
        for body_coord in snake["body"]:
            all_snakes.append(body_coord)
    next_move = "up"
    move_coords = strategies.convert_direction_to_coords(current_head, next_move)
    isSnakesAvoided = strategies.avoid_self(move_coords, all_snakes)
    assert isSnakesAvoided == False


def test_avoid_self_long_body_move_right():
    current_head = {"x": 3, "y": 2}
    snake = {
        "body":
        [
            {"x": 3, "y": 2},
            {"x": 4, "y": 2},
            {"x": 4, "y": 3},
            {"x": 3, "y": 3},
            {"x": 2, "y": 3},
            {"x": 1, "y": 3},
            {"x": 1, "y": 2},
            {"x": 1, "y": 1},
            {"x": 2, "y": 1},
            {"x": 3, "y": 1}
        ]
    }
    current_body = snake["body"]
    next_move = "right"
    move_coords = strategies.convert_direction_to_coords(
        current_head, next_move)
    isSelfAvoided = strategies.avoid_self(move_coords, current_body)
    assert isSelfAvoided == False


def test_avoid_self_long_body_move_left():
    current_head = {"x": 3, "y": 2}
    snake = {
        "body":
        [
            {"x": 3, "y": 2},
            {"x": 4, "y": 2},
            {"x": 4, "y": 3},
            {"x": 3, "y": 3},
            {"x": 2, "y": 3},
            {"x": 1, "y": 3},
            {"x": 1, "y": 2},
            {"x": 1, "y": 1},
            {"x": 2, "y": 1},
            {"x": 3, "y": 1}
        ]
    }
    current_body = snake["body"]
    next_move = "left"
    move_coords = strategies.convert_direction_to_coords(
        current_head, next_move)
    isSelfAvoided = strategies.avoid_self(move_coords, current_body)
    assert isSelfAvoided == True

def test_safe_move_short_body():
    my_head = {"x": 0, "y": 1}
    snake = {
        "body":
        [
            {"x": 0, "y": 1},
            {"x": 0, "y": 0},
            {"x": 1, "y": 0},
            {"x": 1, "y": 1}
        ]
    }
    current_body = snake["body"]
    next_move = "left" # into wall
    move_coords = strategies.convert_direction_to_coords(
        my_head, next_move)
    isSafeMove = strategies.safe_move(move_coords, current_body)
    assert isSafeMove == False
    next_move = "right" # into self
    move_coords = strategies.convert_direction_to_coords(
        my_head, next_move)
    isSafeMove = strategies.safe_move(move_coords, current_body)
    assert isSafeMove == False
    next_move = "down" # into self
    move_coords = strategies.convert_direction_to_coords(
        my_head, next_move)
    isSafeMove = strategies.safe_move(move_coords, current_body)
    assert isSafeMove == False
    next_move = "up" # open grid location
    move_coords = strategies.convert_direction_to_coords(
        my_head, next_move)
    isSafeMove = strategies.safe_move(move_coords, current_body)
    assert isSafeMove == True
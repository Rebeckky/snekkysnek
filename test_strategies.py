import global_variables
import strategies

data = {
    "game": {
        "id": "game-00fe20da-94ad-11ea-bb37",
        "ruleset": {"name": "standard", "version": "v.1.2.3"},
        "timeout": 500,
    },
    "turn": 14,
    "board": {
        "height": 11,
        "width": 11,
        "food": [{"x": 5, "y": 5}, {"x": 9, "y": 0}, {"x": 2, "y": 6}],
        "hazards": [{"x": 3, "y": 2}],
        "snakes": [
            {
                "id": "snake-508e96ac-94ad-11ea-bb37",
                "name": "My Snake",
                "health": 54,
                "body": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}],
                "latency": "111",
                "head": {"x": 0, "y": 0},
                "length": 3,
                "shout": "why are we shouting??",
                "squad": "",
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
                    {"x": 0, "y": 1},
                ],
                "latency": "111",
                "head": {"x": 2, "y": 3},
                "length": 5,
                "shout": "why are we shouting??",
                "squad": "",
            },
            {
                "id": "snake-b67f4906-94ae-11ea-bb37",
                "name": "Another Snake",
                "health": 16,
                "body": [
                    {"x": 5, "y": 4},
                    {"x": 5, "y": 3},
                    {"x": 6, "y": 3},
                    {"x": 6, "y": 2},
                ],
                "latency": "222",
                "head": {"x": 5, "y": 4},
                "length": 4,
                "shout": "I'm not really sure...",
                "squad": "",
            },
        ],
    },
    "you": {
        "id": "snake-508e96ac-94ad-11ea-bb37",
        "name": "My Snake",
        "health": 54,
        "body": [{"x": 0, "y": 0}, {"x": 1, "y": 0}, {"x": 2, "y": 0}],
        "latency": "111",
        "head": {"x": 0, "y": 0},
        "length": 3,
        "shout": "why are we shouting??",
        "squad": "",
    },
}

global_variables.BOARD_MAXIMUM_X = data["board"]["width"]
global_variables.BOARD_MAXIMUM_Y = data["board"]["height"]


def test_avoid_walls_direction_up():

    current_head = data["you"]["head"]
    next_move = "up"
    move_coords = strategies.convert_direction_to_coords(current_head, next_move)
    is_wall_avoided = strategies.avoid_walls(move_coords)
    assert is_wall_avoided == True


def test_avoid_walls_direction_down():

    current_head = data["you"]["head"]
    next_move = "down"
    move_coords = strategies.convert_direction_to_coords(current_head, next_move)
    is_wall_avoided = strategies.avoid_walls(move_coords)
    assert is_wall_avoided == False


def test_avoid_walls_direction_left():

    current_head = data["you"]["head"]
    next_move = "left"
    move_coords = strategies.convert_direction_to_coords(current_head, next_move)
    is_wall_avoided = strategies.avoid_walls(move_coords)
    assert is_wall_avoided == False


def test_avoid_walls_direction_right():

    current_head = data["you"]["head"]
    next_move = "right"
    move_coords = strategies.convert_direction_to_coords(current_head, next_move)
    is_wall_avoided = strategies.avoid_walls(move_coords)
    assert is_wall_avoided == True


def test_avoid_snakes_move_right():
    current_head = data["you"]["head"]
    current_body = data["you"]["body"]
    next_move = "right"
    move_coords = strategies.convert_direction_to_coords(current_head, next_move)
    is_self_avoided = strategies.avoid_snakes(move_coords, current_body)
    assert is_self_avoided == False


def test_avoid_self_move_left():
    current_head = data["you"]["head"]
    current_body = data["you"]["body"]
    next_move = "left"
    move_coords = strategies.convert_direction_to_coords(current_head, next_move)
    is_self_avoided = strategies.avoid_snakes(move_coords, current_body)
    assert is_self_avoided == True


def test_avoid_self_move_up():
    current_head = data["you"]["head"]
    current_body = data["you"]["body"]
    next_move = "up"
    move_coords = strategies.convert_direction_to_coords(current_head, next_move)
    is_self_avoided = strategies.avoid_snakes(move_coords, current_body)
    assert is_self_avoided == True


def test_avoid_self_move_down():
    current_head = data["you"]["head"]
    current_body = data["you"]["body"]
    next_move = "down"
    move_coords = strategies.convert_direction_to_coords(current_head, next_move)
    is_self_avoided = strategies.avoid_snakes(move_coords, current_body)
    assert is_self_avoided == True


def test_avoid_snakes():
    current_head = data["you"]["head"]
    all_snakes = strategies.get_snake_loc_data(data["board"]["snakes"])

    next_move = "up"
    move_coords = strategies.convert_direction_to_coords(current_head, next_move)
    is_snakes_avoided = strategies.avoid_snakes(move_coords, all_snakes)
    assert is_snakes_avoided == False

    next_move = "right"
    move_coords = strategies.convert_direction_to_coords(current_head, next_move)
    is_snakes_avoided = strategies.avoid_snakes(move_coords, all_snakes)
    assert is_snakes_avoided == False


def test_avoid_snakes_long_body_move_right():
    current_head = {"x": 3, "y": 2}
    snake = {
        "body": [
            {"x": 3, "y": 2},
            {"x": 4, "y": 2},
            {"x": 4, "y": 3},
            {"x": 3, "y": 3},
            {"x": 2, "y": 3},
            {"x": 1, "y": 3},
            {"x": 1, "y": 2},
            {"x": 1, "y": 1},
            {"x": 2, "y": 1},
            {"x": 3, "y": 1},
        ]
    }
    current_body = snake["body"]
    next_move = "right"
    move_coords = strategies.convert_direction_to_coords(current_head, next_move)
    is_self_avoided = strategies.avoid_snakes(move_coords, current_body)
    assert is_self_avoided == False


def test_avoid_snakes_long_body_move_left():
    current_head = {"x": 3, "y": 2}
    snake = {
        "body": [
            {"x": 3, "y": 2},
            {"x": 4, "y": 2},
            {"x": 4, "y": 3},
            {"x": 3, "y": 3},
            {"x": 2, "y": 3},
            {"x": 1, "y": 3},
            {"x": 1, "y": 2},
            {"x": 1, "y": 1},
            {"x": 2, "y": 1},
            {"x": 3, "y": 1},
        ]
    }
    current_body = snake["body"]
    next_move = "left"
    move_coords = strategies.convert_direction_to_coords(current_head, next_move)
    is_self_avoided = strategies.avoid_snakes(move_coords, current_body)
    assert is_self_avoided == True


def test_safe_move_all_moves_unsafe():
    next_move = "up"
    is_safe_move = strategies.safe_move(next_move, data)
    assert is_safe_move == False

    next_move = "down"
    is_safe_move = strategies.safe_move(next_move, data)
    assert is_safe_move == False

    next_move = "left"
    is_safe_move = strategies.safe_move(next_move, data)
    assert is_safe_move == False

    next_move = "right"
    is_safe_move = strategies.safe_move(next_move, data)
    assert is_safe_move == False


def test_safe_move_short_body():
    test_data = {
        "you": {"head": {"x": 5, "y": 2}},
        "board": {
            "snakes": [
                {
                    "id": "snake-508e96ac-94ad-11ea-bb37",
                    "name": "My Snake",
                    "health": 54,
                    "body": [{"x": 5, "y": 2}, {"x": 5, "y": 1}, {"x": 5, "y": 1}],
                    "latency": "111",
                    "head": {"x": 5, "y": 2},
                    "length": 3,
                    "shout": "why are we shouting??",
                    "squad": "",
                },
                {
                    "id": "snake-508e96ac-94ad-1639-be12",
                    "name": "Snaaaaake",
                    "health": 54,
                    "body": [
                        {"x": 3, "y": 3},
                        {"x": 2, "y": 3},
                        {"x": 2, "y": 2},
                        {"x": 2, "y": 1},
                        {"x": 1, "y": 1},
                        {"x": 0, "y": 1},
                    ],
                    "latency": "111",
                    "head": {"x": 3, "y": 3},
                    "length": 6,
                    "shout": "why are we shouting??",
                    "squad": "",
                },
                {
                    "id": "snake-508e96ac-94ad-11ea-bb37",
                    "name": "Snek 3",
                    "health": 54,
                    "body": [
                        {"x": 5, "y": 4},
                        {"x": 5, "y": 3},
                        {"x": 6, "y": 3},
                        {"x": 6, "y": 2},
                    ],
                    "latency": "111",
                    "head": {"x": 5, "y": 4},
                    "length": 4,
                    "shout": "why are we shouting??",
                    "squad": "",
                },
            ],
            "game": {},
        },
    }
    global_variables.MY_SNAKE_ID = test_data["board"]["snakes"][0]["id"]
    next_move = "left"  # possible head-to-head collision
    is_safe_move = strategies.safe_move(next_move, test_data)
    assert is_safe_move == True

    next_move = "right"  # possible snake collision
    is_safe_move = strategies.safe_move(next_move, test_data)
    assert is_safe_move == False

    next_move = "down"  # into self
    is_safe_move = strategies.safe_move(next_move, test_data)
    assert is_safe_move == False

    next_move = "up"  # open grid location
    is_safe_move = strategies.safe_move(next_move, test_data)
    assert is_safe_move == False


def test_avoid_head_to_head_collision_unsafe_move():
    my_head = {"x": 3, "y": 4}
    current_snakes = [
        {
            "id": "snake-508e96ac-94ad-11ea-bb37",
            "name": "My Snake",
            "health": 54,
            "body": [
                {"x": 3, "y": 4},
                {"x": 4, "y": 4},
                {"x": 4, "y": 3},
                {"x": 4, "y": 2},
            ],
            "latency": "111",
            "head": {"x": 3, "y": 4},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "",
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
                {"x": 0, "y": 1},
            ],
            "latency": "111",
            "head": {"x": 2, "y": 3},
            "length": 5,
            "shout": "why are we shouting??",
            "squad": "",
        },
    ]
    global_variables.MY_SNAKE_ID = current_snakes[0]["id"]
    next_move = "left"
    move_coords = strategies.convert_direction_to_coords(my_head, next_move)
    is_head_collision_avoided = strategies.avoid_head_to_head_collision(
        move_coords, current_snakes
    )
    assert is_head_collision_avoided == False
    next_move = "down"
    move_coords = strategies.convert_direction_to_coords(my_head, next_move)
    is_head_collision_avoided = strategies.avoid_head_to_head_collision(
        move_coords, current_snakes
    )
    assert is_head_collision_avoided == False


def test_avoid_head_to_head_collision_safe_move():
    my_head = {"x": 4, "y": 4}
    current_snakes = [
        {
            "id": "snake-508e96ac-94ad-11ea-bb37",
            "name": "My Snake",
            "health": 54,
            "body": [{"x": 4, "y": 4}, {"x": 4, "y": 3}, {"x": 4, "y": 2}],
            "latency": "111",
            "head": {"x": 4, "y": 4},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "",
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
                {"x": 0, "y": 1},
            ],
            "latency": "111",
            "head": {"x": 2, "y": 3},
            "length": 5,
            "shout": "why are we shouting??",
            "squad": "",
        },
    ]
    global_variables.MY_SNAKE_ID = current_snakes[0]["id"]
    next_move = "left"
    move_coords = strategies.convert_direction_to_coords(my_head, next_move)
    is_head_collision_avoided = strategies.avoid_head_to_head_collision(
        move_coords, current_snakes
    )
    assert is_head_collision_avoided == True
    next_move = "up"
    move_coords = strategies.convert_direction_to_coords(my_head, next_move)
    is_head_collision_avoided = strategies.avoid_head_to_head_collision(
        move_coords, current_snakes
    )
    assert is_head_collision_avoided == True


def test_avoid_head_to_head_collision_safe_move():
    my_head = {"x": 5, "y": 1}
    current_snakes = [
        {
            "id": "snake-508e96ac-94ad-11ea-bb37",
            "name": "My Snake",
            "health": 54,
            "body": [{"x": 5, "y": 1}, {"x": 5, "y": 1}, {"x": 5, "y": 1}],
            "latency": "111",
            "head": {"x": 5, "y": 1},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "",
        },
        {
            "id": "snake-508e96ac-94ad-1639-be12",
            "name": "Snaaaaake",
            "health": 54,
            "body": [
                {"x": 1, "y": 1},
                {"x": 1, "y": 1},
                {"x": 1, "y": 1},
            ],
            "latency": "111",
            "head": {"x": 1, "y": 1},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "",
        },
    ]
    global_variables.MY_SNAKE_ID = current_snakes[0]["id"]

    next_move = "left"
    move_coords = strategies.convert_direction_to_coords(my_head, next_move)
    is_head_collision_avoided = strategies.avoid_head_to_head_collision(
        move_coords, current_snakes
    )
    assert is_head_collision_avoided == True

    next_move = "right"
    move_coords = strategies.convert_direction_to_coords(my_head, next_move)
    is_head_collision_avoided = strategies.avoid_head_to_head_collision(
        move_coords, current_snakes
    )
    assert is_head_collision_avoided == True
    next_move = "up"
    move_coords = strategies.convert_direction_to_coords(my_head, next_move)
    is_head_collision_avoided = strategies.avoid_head_to_head_collision(
        move_coords, current_snakes
    )
    assert is_head_collision_avoided == True

    next_move = "down"
    move_coords = strategies.convert_direction_to_coords(my_head, next_move)
    is_head_collision_avoided = strategies.avoid_head_to_head_collision(
        move_coords, current_snakes
    )
    assert is_head_collision_avoided == True
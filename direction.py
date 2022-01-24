def direction(facing: str, turn: int):
    directions = ["N", "NE", "E", "SE", "S", "SW", "W", "NW"]

    if not isinstance(facing, str):
        raise TypeError("Facing sould be str type")

    facing = facing.upper()

    if not isinstance(turn, int):
        raise TypeError("Turn sould be int type")

    if facing not in directions:
        raise Exception("Please enter valid data")

    if turn % 45 != 0:
        raise Exception("Turn must be divisible by 45 without a remainder")

    steps = turn / 45

    if steps % 8 == 0:
        return facing
    else:
        return directions[int(directions.index(facing) + steps) % 8]

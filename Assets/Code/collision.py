from Assets.Code import constants


def is_colliding(player_x, player_y, colliders, to_execute):
    """To execute is a function."""
    if (player_x, player_y) in colliders:
        to_execute()


def push(player_x, player_y, direction: int):
    if direction == constants.UP:
        return player_x, player_y - 1

    if direction == constants.DOWN:
        return player_x, player_y + 1

    if direction == constants.LEFT:
        return player_x - 1, player_y

    if direction == constants.RIGHT:
        return player_x + 1, player_y

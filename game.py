import fusionengine as engine
from Assets.Code import objects

count = 0

lvl_width, lvl_height = 3, 1
tile_width, tile_height = 128, 128
player_x, player_y = 0, 0
goal_x, goal_y = 2, 0

main = engine.Main()

lvl_1 = main.window.new_window('Level 1', lvl_width * tile_width, lvl_height * tile_height)
main.window.change_icon('Assets/Images/player.png')

while main.window.running(lvl_1):
    main.draw.draw_rect(lvl_1, 0, 0, lvl_width * tile_width, lvl_height * tile_height, (0, 0, 0, 255))
    if main.event.key_down(main.keys.KEY_w):
        count += 1
        if count == 1:
            player_y -= 1

    elif main.event.key_down(main.keys.KEY_a):
        count += 1
        if count == 1:
            player_x -= 1

    elif main.event.key_down(main.keys.KEY_s):
        count += 1
        if count == 1:
            player_y += 1

    elif main.event.key_down(main.keys.KEY_d):
        count += 1
        if count == 1:
            player_x += 1

    else:
        count = 0

    if player_x < 0:
        player_x = 0

    if player_x >= lvl_width:
        player_x = lvl_width - 1

    if player_y < 0:
        player_y = 0

    if player_y >= lvl_height:
        player_y = lvl_height - 1

    objects.draw_object(
        lvl_1,
        'Assets/Images/player.png',
        player_x * tile_width,
        player_y * tile_height,
        tile_width,
        tile_height,
        main
    )

    objects.draw_object(
        lvl_1,
        'Assets/Images/goal.png',
        goal_x * tile_width,
        goal_y * tile_height,
        tile_width,
        tile_height,
        main
    )

    if player_x == goal_x and player_y == goal_y:
        break

lvl_width, lvl_height = 5, 3
tile_width, tile_height = 92, 92
player_x, player_y = 0, 2
goal_x, goal_y = 4, 0

walls = [(1, 1), (1, 2), (3, 0), (3, 1)]

main = engine.Main()


lvl_2 = main.window.new_window('Level 2', lvl_width * tile_width, lvl_height * tile_height)
main.window.change_icon('Assets/Images/player.png')


def up():
    global player_y
    player_y -= 1


def down():
    global player_y
    player_y += 1


def left():
    global player_x
    player_x -= 1


def right():
    global player_x
    player_x += 1


while main.window.running(lvl_2):
    main.draw.draw_rect(lvl_2, 0, 0, lvl_width * tile_width, lvl_height * tile_height, (0, 0, 0, 255))
    if main.event.key_down(main.keys.KEY_w):
        count += 1
        if count == 1:
            player_y -= 1

    elif main.event.key_down(main.keys.KEY_a):
        count += 1
        if count == 1:
            player_x -= 1

    elif main.event.key_down(main.keys.KEY_s):
        count += 1
        if count == 1:
            player_y += 1

    elif main.event.key_down(main.keys.KEY_d):
        count += 1
        if count == 1:
            player_x += 1

    else:
        count = 0

    if player_x < 0:
        player_x = 0

    if player_x >= lvl_width:
        player_x = lvl_width - 1

    if player_y < 0:
        player_y = 0

    if player_y >= lvl_height:
        player_y = lvl_height - 1

    objects.draw_object(
        lvl_2,
        'Assets/Images/player.png',
        player_x * tile_width,
        player_y * tile_height,
        tile_width,
        tile_height,
        main
    )

    objects.draw_object(
        lvl_2,
        'Assets/Images/goal.png',
        goal_x * tile_width,
        goal_y * tile_height,
        tile_width,
        tile_height,
        main
    )

    for wall in walls:
        objects.draw_object(
            lvl_2,
            'Assets/Images/wall.png',
            wall[0] * tile_width,
            wall[1] * tile_height,
            tile_width,
            tile_height,
            main
        )

    if player_x == goal_x and player_y == goal_y:
        break

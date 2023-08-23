import fusionengine as engine
from fusionengine.files.window import _CustomRenderer as winobj
from Assets.Code import objects

count = 0

lvl_width, lvl_height = 3, 1
tile_width, tile_height = 128, 128
player_x, player_y = 0, 0
goal_x, goal_y = 2, 0

tb, to = False, False  # if blue and orange are triggered
blue_t, orange_t = [], []  # blue and orange triggers
blue_w, orange_w = [], []  # blue and orange walls

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

tb, to = False, False
blue_t, orange_t = [], []
blue_w, orange_w = [], []
walls = [(1, 1), (1, 2), (3, 0), (3, 1)]

main = engine.Main()


lvl_2 = main.window.new_window('Level 2', lvl_width * tile_width, lvl_height * tile_height)
main.window.change_icon('Assets/Images/player.png')


def movement_check():
    global player_x, player_y, tb, to, count
    prev_x, prev_y = player_x, player_y
    if main.event.key_down(main.keys.KEY_w):
        count += 1
        if count == 1:
            player_y -= 1
            if (player_x, player_y) in walls:
                player_y = prev_y

            if (player_x, player_y) in blue_w and not tb:
                player_y = prev_y

            if (player_x, player_y) in orange_w and not to:
                player_y = prev_y

            if (player_x, player_y) in blue_t:
                tb = not tb

            if (player_x, player_y) in orange_t:
                to = not to

    elif main.event.key_down(main.keys.KEY_a):
        count += 1
        if count == 1:
            player_x -= 1
            if (player_x, player_y) in walls:
                player_x = prev_x

            if (player_x, player_y) in blue_w and tb:
                player_x = prev_x

            if (player_x, player_y) in orange_w and to:
                player_x = prev_x

            if (player_x, player_y) in blue_t:
                tb = not tb

            if (player_x, player_y) in orange_t:
                to = not to

    elif main.event.key_down(main.keys.KEY_s):
        count += 1
        if count == 1:
            player_y += 1
            if (player_x, player_y) in walls:
                player_y = prev_y

            if (player_x, player_y) in blue_w and not tb:
                player_y = prev_y

            if (player_x, player_y) in orange_w and not to:
                player_y = prev_y

            if (player_x, player_y) in blue_t:
                tb = not tb

            if (player_x, player_y) in orange_t:
                to = not to

    elif main.event.key_down(main.keys.KEY_d):
        count += 1
        if count == 1:
            player_x += 1
            if (player_x, player_y) in walls:
                player_x = prev_x

            if (player_x, player_y) in blue_w and not tb:
                player_x = prev_x

            if (player_x, player_y) in orange_w and not to:
                player_x = prev_x

            if (player_x, player_y) in blue_t:
                tb = not tb

            if (player_x, player_y) in orange_t:
                to = not to

    else:
        count = 0

    if player_x < 0:
        player_x = prev_x

    if player_x >= lvl_width:
        player_x = prev_x

    if player_y < 0:
        player_y = prev_y

    if player_y >= lvl_height:
        player_y = prev_y


def draw_all(window: winobj):
    objects.draw_object(
        window,
        'Assets/Images/goal.png',
        goal_x * tile_width,
        goal_y * tile_height,
        tile_width,
        tile_height,
        main
    )

    for wall in walls:
        objects.draw_object(
            window,
            'Assets/Images/wall.png',
            wall[0] * tile_width,
            wall[1] * tile_height,
            tile_width,
            tile_height,
            main
        )

    for bt in blue_t:
        objects.draw_object(
            window,
            'Assets/Images/trigger_blue.png',
            bt[0] * tile_width,
            bt[1] * tile_height,
            tile_width,
            tile_height,
            main
        )

    for ot in orange_t:
        objects.draw_object(
            window,
            'Assets/Images/trigger_orange.png',
            ot[0] * tile_width,
            ot[1] * tile_height,
            tile_width,
            tile_height,
            main
        )

    for bw in blue_w:
        objects.draw_object(
            window,
            'Assets/Images/trigger_wall_blue.png' if not tb else 'Assets/Images/tw_blue_off.png',
            bw[0] * tile_width,
            bw[1] * tile_height,
            tile_width,
            tile_height,
            main
        )

    for ow in orange_w:
        objects.draw_object(
            window,
            'Assets/Images/tw_orange.png' if not tb else 'Assets/Images/tw_orange_off.png',
            ow[0] * tile_width,
            ow[1] * tile_height,
            tile_width,
            tile_height,
            main
        )

    objects.draw_object(
        window,
        'Assets/Images/player.png',
        player_x * tile_width,
        player_y * tile_height,
        tile_width,
        tile_height,
        main
    )


while main.window.running(lvl_2):
    main.draw.draw_rect(lvl_2, 0, 0, lvl_width * tile_width, lvl_height * tile_height, (0, 0, 0, 255))
    movement_check()
    draw_all(lvl_2)

    if player_x == goal_x and player_y == goal_y:
        break

lvl_width, lvl_height = 5, 3
tile_width, tile_height = 92, 92
player_x, player_y = 0, 0
goal_x, goal_y = 4, 2

tb, to = False, False
blue_t, orange_t = [(4, 0)], []
blue_w, orange_w = [(3, 1), (4, 1), (3, 2)], []
walls = []

lvl_3 = main.window.new_window('Level 3', lvl_width * tile_width, lvl_height * tile_height)
main.window.change_icon('Assets/Images/player.png')

while main.window.running(lvl_3):
    main.draw.draw_rect(lvl_3, 0, 0, lvl_width * tile_width, lvl_height * tile_height, (0, 0, 0, 255))
    movement_check()
    draw_all(lvl_3)

    if player_x == goal_x and player_y == goal_y:
        break

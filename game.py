import fusionengine as engine
from fusionengine.files.window import _CustomRenderer as winobj
from Assets.Code import objects

count = 0


def movement_check():
    global player_x, player_y, px_init, py_init, holes, tb, to, count
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
            
            if (player_x, player_y) in holes:
                player_x, player_y = px_init, py_init;
                tb, to = False;

    elif main.event.key_down(main.keys.KEY_a):
        count += 1
        if count == 1:
            player_x -= 1
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
            
            if (player_x, player_y) in holes:
                player_x, player_y = px_init, py_init;
                tb, to = False;

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

            if (player_x, player_y) in holes:
                player_x, player_y = px_init, py_init;
                tb, to = False;

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
            
            if (player_x, player_y) in holes:
                player_x, player_y = px_init, py_init;
                tb, to = False, False;

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
            'Assets/Images/tw_orange.png' if not to else 'Assets/Images/tw_orange_off.png',
            ow[0] * tile_width,
            ow[1] * tile_height,
            tile_width,
            tile_height,
            main
        )
    
    for hole in holes:
        objects.draw_object(
            window,
            'Assets/Images/hole.png',
            hole[0] * tile_width,
            hole[1] * tile_height,
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

# Level 1

lvl_width, lvl_height = 3, 1
tile_width, tile_height = 128, 128
player_x, player_y = 0, 0
px_init, py_init = player_x, player_y
goal_x, goal_y = 2, 0

tb, to = False, False  # whether blue and orange are triggered
blue_t, orange_t = [], []  # blue and orange triggers
blue_w, orange_w = [], []  # blue and orange walls
walls = []
holes = []

main = engine.Main()
main.window.toggle_quittable()  # Make it so that quitting is not possible by 'X' button

lvl_1 = main.window.new_window('Level 1', lvl_width * tile_width, lvl_height * tile_height)
main.window.change_icon('Assets/Images/player.png')

while main.window.running(lvl_1):
    main.draw.draw_rect(lvl_1, 0, 0, lvl_width * tile_width, lvl_height * tile_height, (0, 0, 0, 255))

    movement_check()
    draw_all(lvl_1)

    if player_x == goal_x and player_y == goal_y:
        break

# Level 2

lvl_width, lvl_height = 5, 3
tile_width, tile_height = 92, 92
player_x, player_y = 0, 2
px_init, py_init = player_x, player_y
goal_x, goal_y = 4, 0

tb, to = False, False
blue_t, orange_t = [], []
blue_w, orange_w = [], []
holes = []
walls = [(1, 1), (1, 2), (3, 0), (3, 1)]

lvl_2 = main.window.new_window('Level 2', lvl_width * tile_width, lvl_height * tile_height)
main.window.change_icon('Assets/Images/player.png')

while main.window.running(lvl_2):
    main.draw.draw_rect(lvl_2, 0, 0, lvl_width * tile_width, lvl_height * tile_height, (0, 0, 0, 255))

    movement_check()
    draw_all(lvl_2)

    if player_x == goal_x and player_y == goal_y:
        break

# Level 3

lvl_width, lvl_height = 5, 3
tile_width, tile_height = 96, 96
player_x, player_y = 0, 0
px_init, py_init = player_x, player_y
goal_x, goal_y = 4, 2

tb, to = False, False
blue_t, orange_t = [(4, 0)], []
blue_w, orange_w = [(3, 1), (4, 1), (3, 2)], []
holes = []
walls = []

lvl_3 = main.window.new_window('Level 3', lvl_width * tile_width, lvl_height * tile_height)
main.window.change_icon('Assets/Images/player.png')

while main.window.running(lvl_3):
    main.draw.draw_rect(lvl_3, 0, 0, lvl_width * tile_width, lvl_height * tile_height, (0, 0, 0, 255))

    movement_check()
    draw_all(lvl_3)

    if player_x == goal_x and player_y == goal_y:
        break

# Level 4

lvl_width, lvl_height = 10, 6
tile_width, tile_height = 64, 64
player_x, player_y = 0, 0
px_init, py_init = player_x, player_y
goal_x, goal_y = 9, 0

lvl_4 = main.window.new_window('Level 4', lvl_width * tile_width, lvl_height * tile_height)
main.window.change_icon('Assets/Images/player.png')
tb, to = False, False
blue_t, orange_t = [(2, 5)], [(7, 0)]
blue_w, orange_w = [(6, 0), (6, 1), (6, 2), (7, 2), (8, 2), (9, 2)], [(8, 0), (8, 1), (9, 1)]
holes = [(5, 5)]
walls = []


while main.window.running(lvl_4):
    main.draw.draw_rect(lvl_3, 0, 0, lvl_width * tile_width, lvl_height * tile_height, (0, 0, 0, 255))

    movement_check()
    draw_all(lvl_4)

    if player_x == goal_x and player_y == goal_y:
        break

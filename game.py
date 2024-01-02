import fusionengine as engine
from Assets.Code import objects

count = 0

type winobj = engine.Window


def movement_check():
    global player_x, player_y, px_init, py_init, holes, tb, to, count, last_enabled_checkpoint
    prev_x, prev_y = player_x, player_y
    if engine.Key(engine.KEY_w).key_down() or engine.Key(engine.KEY_UP).key_down():
        count += 1
        if count == 1:
            player_y -= 1

    elif engine.Key(engine.KEY_a).key_down() or engine.Key(engine.KEY_LEFT).key_down():
        count += 1
        if count == 1:
            player_x -= 1

    elif engine.Key(engine.KEY_s).key_down() or engine.Key(engine.KEY_DOWN).key_down():
        count += 1
        if count == 1:
            player_y += 1

    elif engine.Key(engine.KEY_d).key_down() or engine.Key(engine.KEY_RIGHT).key_down():
        count += 1
        if count == 1:
            player_x += 1

    else:
        count = 0

    if count == 1:
        if (player_x, player_y) in walls:
            player_x, player_y = prev_x, prev_y

        if (player_x, player_y) in blue_w and not tb:
            player_x, player_y = prev_x, prev_y

        if (player_x, player_y) in orange_w and not to:
            player_x, player_y = prev_x, prev_y

        if (player_x, player_y) in blue_t:
            tb = not tb

        if (player_x, player_y) in orange_t:
            to = not to
        
        if (player_x, player_y) in holes:
            player_x, player_y = px_init, py_init
            tb, to = False, False

        if (player_x, player_y) in checkpoints:
            px_init, py_init = player_x, player_y
            last_enabled_checkpoint = checkpoints.index((player_x, player_y))

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
        tile_height
    )

    for wall in walls:
        objects.draw_object(
            window,
            'Assets/Images/wall.png',
            wall[0] * tile_width,
            wall[1] * tile_height,
            tile_width,
            tile_height
        )

    for bt in blue_t:
        objects.draw_object(
            window,
            'Assets/Images/trigger_blue.png',
            bt[0] * tile_width,
            bt[1] * tile_height,
            tile_width,
            tile_height
        )

    for ot in orange_t:
        objects.draw_object(
            window,
            'Assets/Images/trigger_orange.png',
            ot[0] * tile_width,
            ot[1] * tile_height,
            tile_width,
            tile_height
        )

    for bw in blue_w:
        objects.draw_object(
            window,
            'Assets/Images/trigger_wall_blue.png' if not tb else 'Assets/Images/tw_blue_off.png',
            bw[0] * tile_width,
            bw[1] * tile_height,
            tile_width,
            tile_height
        )

    for ow in orange_w:
        objects.draw_object(
            window,
            'Assets/Images/tw_orange.png' if not to else 'Assets/Images/tw_orange_off.png',
            ow[0] * tile_width,
            ow[1] * tile_height,
            tile_width,
            tile_height
        )
    
    for hole in holes:
        objects.draw_object(
            window,
            'Assets/Images/hole.png',
            hole[0] * tile_width,
            hole[1] * tile_height,
            tile_width,
            tile_height
        )

    for idx, checkpoint in enumerate(checkpoints):
        if idx == last_enabled_checkpoint:
            objects.draw_object(
                window,
                'Assets/Images/checkpoint_on.png',
                checkpoint[0] * tile_width,
                checkpoint[1] * tile_height,
                tile_width,
                tile_height
            )
        else:
            objects.draw_object(
                window,
                'Assets/Images/checkpoint_off.png',
                checkpoint[0] * tile_width,
                checkpoint[1] * tile_height,
                tile_width,
                tile_height
            )

    objects.draw_object(
        window,
        'Assets/Images/player.png',
        player_x * tile_width,
        player_y * tile_height,
        tile_width,
        tile_height
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
checkpoints = []; last_enabled_checkpoint = -1

lvl_1 = engine.Window('Level 1', lvl_width * tile_width, lvl_height * tile_height)
lvl_1.change_icon('Assets/Images/player.png')
lvl_1.toggle_quittable()  # X button cannot close

while lvl_1.running():
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
checkpoints = []; last_enabled_checkpoint = -1

lvl_2 = engine.Window('Level 2', lvl_width * tile_width, lvl_height * tile_height)
lvl_2.change_icon('Assets/Images/player.png')
lvl_2.toggle_quittable()

while lvl_2.running():
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
checkpoints = []; last_enabled_checkpoint = -1

lvl_3 = engine.Window('Level 3', lvl_width * tile_width, lvl_height * tile_height)
lvl_3.change_icon('Assets/Images/player.png')
lvl_3.toggle_quittable()

while lvl_3.running():
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

lvl_4 = engine.Window('Level 4', lvl_width * tile_width, lvl_height * tile_height)
lvl_4.change_icon('Assets/Images/player.png')
lvl_4.toggle_quittable()
tb, to = False, False
blue_t, orange_t = [(2, 5)], [(7, 0)]
blue_w, orange_w = [(6, 0), (6, 1), (6, 2), (7, 2), (8, 2), (9, 2)], [(8, 0), (8, 1), (9, 1)]
holes = [(5, 5)]
walls = []
checkpoints = [(4, 4)]
last_enabled_checkpoint = -1 # Index of enabled checkpoint

while lvl_4.running():
    movement_check()
    draw_all(lvl_4)

    if player_x == goal_x and player_y == goal_y:
        break


lvl_width, lvl_height = 10, 6
tile_width, tile_height = 64, 64
player_x, player_y = 0, 0
px_init, py_init = player_x, player_y
goal_x, goal_y = 6, 3

lvl_5 = engine.Window('Level 5', lvl_width * tile_width, lvl_height * tile_height)
lvl_5.change_icon('Assets/Images/player.png')
lvl_5.toggle_quittable()
tb, to = False, False
blue_t, orange_t = [(9, 0)], []
blue_w, orange_w = [(6, 2), (5, 2), (5, 3), (5, 4), (5, 5)], []
holes = [(3, 3)]
walls = [(7, 2), (7, 3), (7, 4), (7, 5), (6, 5)]
checkpoints = [(3, 2), (6, 4)]
last_enabled_checkpoint = -1

while lvl_5.running():
    movement_check()
    draw_all(lvl_4)

    if player_x == goal_x and player_y == goal_y:
        break

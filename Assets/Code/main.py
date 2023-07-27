import fusionengine as engine
import collision

main = engine.Main()

tile_width, tile_height = 48, 48

lvl_width, lvl_height = 10, 6

window = main.window.new_window('a little game', tile_width * lvl_width, tile_height * lvl_height)

x = 0
y = 0

blue_triggered = False
orange_triggered = False
walls = [(X, 4) for X in range(4, 10)]

blue_walls = [(8, 3), (8, 2), (9, 2), (7, 5)]
blue_triggers = [(6, 2)]
blue_open_triggers = [(6, 3)]

orange_walls = [(8, 5)]
orange_triggers = [(9, 3)]
orange_open_triggers = []

goal_pos = (9, 5)


def draw_object(location, image, tile_width, tile_height):
    ox, oy = location
    obj_img = main.image.open_image(window, image, ox * tile_width, oy * tile_height, tile_width, tile_height)
    main.image.draw_image(obj_img)


def draw_objects(locations, image, tile_width, tile_height):
    for location in locations:
        draw_object(location, image, tile_width, tile_height)


def blue_trigger():
    global blue_triggered; blue_triggered = not blue_triggered  # NOQA


def blue_open():
    global blue_triggered; blue_triggered = True  # NOQA


def orange_trigger():
    global orange_triggered; orange_triggered = not orange_triggered  # NOQA


def orange_open():
    global orange_triggered; orange_triggered = True  # NOQA


def down():
    global y
    y += 1


def up():
    global y
    y -= 1


def right():
    global x
    x += 1


def left():
    global x
    x -= 1


def trigger_collisions():
    collision.is_colliding(x, y, blue_triggers, blue_trigger)
    collision.is_colliding(x, y, blue_open_triggers, blue_open)
    collision.is_colliding(x, y, orange_triggers, orange_trigger)
    collision.is_colliding(x, y, orange_open_triggers, orange_open)


@main.window.loop
def loop():
    global x, y

    blockers = walls + (blue_walls if not blue_triggered else []) + (orange_walls if not orange_triggered else [])

    if (x, y) == goal_pos:
        main.quit(window)

    if main.event.key_down(main.keys.KEY_w, window):
        y -= 1
        collision.is_colliding(x, y, blockers, down)
        trigger_collisions()

    elif main.event.key_down(main.keys.KEY_a, window):
        x -= 1
        collision.is_colliding(x, y, blockers, right)
        trigger_collisions()

    elif main.event.key_down(main.keys.KEY_s, window):
        y += 1
        collision.is_colliding(x, y, blockers, up)
        trigger_collisions()

    elif main.event.key_down(main.keys.KEY_d, window):
        x += 1
        collision.is_colliding(x, y, blockers, left)
        trigger_collisions()

    if x < 0:
        x = 0

    if x >= lvl_width:
        x = lvl_width - 1

    if y < 0:
        y = 0

    if y >= lvl_height:
        y = lvl_height - 1

    draw_objects(walls, '../Images/wall.png', tile_width, tile_height)

    draw_objects(blue_walls, '../Images/trigger_wall_blue.png' if not blue_triggered else
                             '../Images/tw_blue_off.png', tile_width, tile_height)
    draw_objects(blue_triggers, '../Images/trigger_blue.png', tile_width, tile_height)
    draw_objects(blue_open_triggers, '../Images/trigger_blue_open.png', tile_width, tile_height)

    draw_objects(orange_walls, '../Images/tw_orange.png' if not orange_triggered else
                               '../Images/tw_orange_off.png', tile_width, tile_height)
    draw_objects(orange_triggers, '../Images/trigger_orange.png', tile_width, tile_height)
    draw_objects(orange_open_triggers, '../Images/trigger_orange_open.png', tile_width, tile_height)

    draw_object(goal_pos, '../Images/goal.png', tile_width, tile_height)

    draw_object((x, y), '../Images/player.png', tile_width, tile_height)

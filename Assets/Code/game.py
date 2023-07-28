import fusionengine as engine
from Assets.Code import collision, objects

lvl_width, lvl_height = 3, 1
tile_width, tile_height = 128, 128
player_x, player_y = 0, 0
goal_x, goal_y = 2, 0

main = engine.Main()

window = main.window.new_window('Level 1', lvl_width * tile_width, lvl_height * tile_height)


@main.window.loop
def loop():
    global player_x, player_y
    if main.event.key_down(main.keys.KEY_w, window):
        player_y -= 1

    if main.event.key_down(main.keys.KEY_a, window):
        player_x -= 1

    if main.event.key_down(main.keys.KEY_s, window):
        player_y += 1

    if main.event.key_down(main.keys.KEY_d, window):
        player_x += 1

    if player_x < 0:
        player_x = 0

    if player_x >= lvl_width:
        player_x = lvl_width - 1

    if player_y < 0:
        player_y = 0

    if player_y >= lvl_height:
        player_y = lvl_height - 1

    objects.draw_object(
        window,
        '../Images/player.png',
        player_x * tile_width,
        player_y * tile_height,
        tile_width,
        tile_height,
        main
    )

    objects.draw_object(
        window,
        '../Images/goal.png',
        goal_x * tile_width,
        goal_y * tile_height,
        tile_width,
        tile_height,
        main
    )

    collision.is_colliding(player_x, player_y, [(goal_x, goal_y)], lambda: main.quit(window))
